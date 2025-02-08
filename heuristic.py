import pandas as pd
from dateutil.parser import parse
import pm4py
from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
from pm4py.visualization.heuristics_net import visualizer as hn_visualizer

file_path = "./BPMN_Process_Log_Enes_Shpetim.csv"
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

print("DataFrame:")
print(df)

# Format the dataframe for PM4Py
log = pm4py.format_dataframe(
    df, case_id="Case_ID", activity_key="Activity", timestamp_key="Timestamp"
)

# Log Summary
total_cases = df["Case_ID"].nunique()
total_events = len(df)
activity_distribution = df["Activity"].value_counts()

print("Log Summary:")
print(f"Total number of cases: {total_cases}")
print(f"Total number of events: {total_events}")
print("Activity distribution:")
print(activity_distribution)

# Apply Heuristic Miner to discover a heuristic net
heuristic_net = heuristics_miner.apply_heu(log)
print("Heuristic net created successfully.")

# Visualize the heuristic net
heuristic_net_image = hn_visualizer.apply(heuristic_net)
hn_visualizer.save(heuristic_net_image, "heuristic.png")
print("Heuristic net visualization saved as heuristic.png")

# Convert heuristic net to Petri net for conformance checking
net, initial_marking, final_marking = pm4py.convert_to_petri_net(heuristic_net)