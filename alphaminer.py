import pandas as pd
from dateutil.parser import parse
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer

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

# Ensure the data is sorted by Case_ID and Timestamp
df.sort_values(by=["Case_ID", "Timestamp"], inplace=True)

print("DataFrame:")
print(df)

# Format the dataframe for PM4Py
log = pm4py.format_dataframe(
    df, case_id="Case_ID", activity_key="Activity", timestamp_key="Timestamp"
)

# Apply Alpha Miner to discover a Petri net
net, initial_marking, final_marking = alpha_miner.apply(log)
print("Alpha Miner applied successfully.")

# Visualize the Petri net
gviz = pn_visualizer.apply(net, initial_marking, final_marking)
pn_visualizer.save(gviz, "alpha_miner_petri_net.png")
print("Petri net visualization saved as alpha_miner_petri_net.png")