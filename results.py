import pandas as pd
from dateutil.parser import parse
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.algo.conformance.tokenreplay import algorithm as token_replay
from pm4py.algo.evaluation.precision import algorithm as precision_evaluator
from pm4py.algo.evaluation.generalization import algorithm as generalization_evaluator
from pm4py.algo.evaluation.simplicity import algorithm as simplicity_evaluator

# Load event log data
file_path = "BPMN_Process_Log_Enes_Shpetim.csv"
df = pd.read_csv(file_path, sep=",")

if "Timestamp" not in df.columns:
    raise KeyError("The 'Timestamp' column is missing from the dataset.")

df["Timestamp"] = df["Timestamp"].str.strip()
df["Timestamp"] = df["Timestamp"].apply(lambda x: parse(x, dayfirst=True))

# Remove rows with missing values in key columns
df.dropna(subset=["Case_ID", "Activity", "Timestamp"], inplace=True)

df["Case_ID"] = df["Case_ID"].astype("string")
df["Activity"] = df["Activity"].astype("string")

df.sort_values(by=["Case_ID", "Timestamp"], inplace=True)

print("✅ DataFrame Loaded:")
print(df.head())

# Convert dataframe into event log format
log = pm4py.format_dataframe(df, case_id="Case_ID", activity_key="Activity", timestamp_key="Timestamp")

### **🚀 Step 1: Apply Alpha Miner**
net_alpha, im_alpha, fm_alpha = alpha_miner.apply(log)

### **🚀 Step 2: Apply Heuristic Miner (With Adjusted Parameters)**
heuristic_net = heuristics_miner.apply_heu(log, parameters={
    "dependency_threshold": 0.3,  # More flexible threshold
    "AND_measure_threshold": 0.4  # Adjusted for parallelism
})
net_heuristic, im_heuristic, fm_heuristic = pm4py.convert_to_petri_net(heuristic_net)

### **🚀 Step 3: Debug Token Replay Failures**
print("\n🔍 Running Token Replay Debugging...")

# Apply Token Replay on Alpha Miner model
trace_replay_results_alpha = token_replay.apply(
    log, net_alpha, im_alpha, fm_alpha,
    parameters={"variant": token_replay.Variants.TOKEN_REPLAY, "approximate": True}
)

# Count total failed traces
failed_traces_alpha = [res for res in trace_replay_results_alpha if res.get("trace_is_fit") == False]
print(f"\n❌ Total failed traces (Alpha Miner): {len(failed_traces_alpha)} / {len(trace_replay_results_alpha)}")

# Apply Token Replay on Heuristic Miner model
trace_replay_results_heuristic = token_replay.apply(
    log, net_heuristic, im_heuristic, fm_heuristic,
    parameters={"variant": token_replay.Variants.TOKEN_REPLAY, "approximate": True}
)

# Count total failed traces
failed_traces_heuristic = [res for res in trace_replay_results_heuristic if res.get("trace_is_fit") == False]
print(f"\n❌ Total failed traces (Heuristic Miner): {len(failed_traces_heuristic)} / {len(trace_replay_results_heuristic)}")

# Extract fitness from Token Replay results
fitness_alpha = sum(trace["trace_fitness"] for trace in trace_replay_results_alpha) / len(trace_replay_results_alpha)
fitness_heuristic = sum(trace["trace_fitness"] for trace in trace_replay_results_heuristic) / len(trace_replay_results_heuristic)

print(f"\n✅ Fitness (Alpha Miner): {fitness_alpha}")
print(f"✅ Fitness (Heuristic Miner): {fitness_heuristic}")

### **🚀 Step 4: Compute Precision, Generalization, and Simplicity**
precision_alpha = precision_evaluator.apply(log, net_alpha, im_alpha, fm_alpha)
precision_heuristic = precision_evaluator.apply(log, net_heuristic, im_heuristic, fm_heuristic)

generalization_alpha = generalization_evaluator.apply(log, net_alpha, im_alpha, fm_alpha)
generalization_heuristic = generalization_evaluator.apply(log, net_heuristic, im_heuristic, fm_heuristic)

simplicity_alpha = simplicity_evaluator.apply(net_alpha)
simplicity_heuristic = simplicity_evaluator.apply(net_heuristic)

### **🚀 Step 5: Save Results to CSV**
evaluation_results = pd.DataFrame({
    "Metric": ["Fitness", "Precision", "Generalization", "Simplicity"],
    "Alpha Miner": [fitness_alpha, precision_alpha, generalization_alpha, simplicity_alpha],
    "Heuristic Miner": [fitness_heuristic, precision_heuristic, generalization_heuristic, simplicity_heuristic]
})

results_path = "final_results.csv"
evaluation_results.to_csv(results_path, index=False)

print(f"\n🚀 Process mining evaluation completed. Results saved to '{results_path}'.")
