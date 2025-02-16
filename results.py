import pandas as pd
from dateutil.parser import parse
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from pm4py.algo.evaluation.generalization import algorithm as generalization_evaluator
from pm4py.algo.evaluation.simplicity import algorithm as simplicity_evaluator
from pm4py.visualization.petri_net import visualizer as pn_visualizer
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer

file_path = "BPMN_Process_Log_Enes_Shpetim.csv"
df = pd.read_csv(file_path, sep=",")

df.dropna(subset=["Case_ID", "Activity", "Timestamp"], inplace=True)
df.sort_values(by=["Case_ID", "Timestamp"], inplace=True)

print(df.head())

log = pm4py.format_dataframe(df, case_id="Case_ID", activity_key="Activity", timestamp_key="Timestamp")

net_alpha, im_alpha, fm_alpha = alpha_miner.apply(log)

heuristic_net = heuristics_miner.apply_heu(log)
net_heuristic, im_heuristic, fm_heuristic = pm4py.convert_to_petri_net(heuristic_net)

trace_replay_results_alpha = token_replay.apply(
    log, net_alpha, im_alpha, fm_alpha,
    parameters={"variant": token_replay.Variants.TOKEN_REPLAY, "approximate": True}
)

trace_replay_results_heuristic = token_replay.apply(
    log, net_heuristic, im_heuristic, fm_heuristic,
    parameters={"variant": token_replay.Variants.TOKEN_REPLAY, "approximate": True}
)

fitness_alpha = sum(trace["trace_fitness"] for trace in trace_replay_results_alpha) / len(trace_replay_results_alpha)
fitness_heuristic = sum(trace["trace_fitness"] for trace in trace_replay_results_heuristic) / len(trace_replay_results_heuristic)

print(f"\nFitness (Alpha Miner): {fitness_alpha}")
print(f"Fitness (Heuristic Miner): {fitness_heuristic}")

precision_alpha = precision_evaluator.apply(log, net_alpha, im_alpha, fm_alpha)
precision_heuristic = precision_evaluator.apply(log, net_heuristic, im_heuristic, fm_heuristic)

generalization_alpha = generalization_evaluator.apply(log, net_alpha, im_alpha, fm_alpha)
generalization_heuristic = generalization_evaluator.apply(log, net_heuristic, im_heuristic, fm_heuristic)

simplicity_alpha = simplicity_evaluator.apply(net_alpha)
simplicity_heuristic = simplicity_evaluator.apply(net_heuristic)

evaluation_results = pd.DataFrame({
    "Metric": ["Fitness", "Precision", "Generalization", "Simplicity"],
    "Alpha Miner": [fitness_alpha, precision_alpha, generalization_alpha, simplicity_alpha],
    "Heuristic Miner": [fitness_heuristic, precision_heuristic, generalization_heuristic, simplicity_heuristic]
})

results_path = "evaluation_results.csv"
evaluation_results.to_csv(results_path, index=False)

print(f"\n🚀 Process mining evaluation completed. Results saved to '{results_path}'.")

# Visualize the heuristic net
heuristic_net_image = hn_visualizer.apply(heuristic_net)
hn_visualizer.save(heuristic_net_image, "heuristic.png")
print("Heuristic net visualization saved as heuristic.png")

# Visualize the Petri net
gviz_alpha = pn_visualizer.apply(net_alpha, im_alpha, fm_alpha)
pn_visualizer.save(gviz_alpha, "alpha_miner_petri_net.png")
print("Petri net visualization saved as alpha_miner_petri_net.png")

