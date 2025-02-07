import pandas as pd
from dateutil.parser import parse
import pm4py
from pm4py.algo.discovery.alpha import algorithm as alpha_miner
from pm4py.visualization.petri_net import visualizer as pn_visualizer

# Load the event log data
file_path = "C:/Users/Admin/Desktop/process_mining/BPMN_Process_Log_Enes_Shpetim.csv"
df = pd.read_csv(file_path, sep=",")

# Check for the 'Timestamp' column
if "Timestamp" not in df.columns:
    raise KeyError("The 'Timestamp' column is missing from the dataset.")

# Strip whitespace from the 'Timestamp' column
df["Timestamp"] = df["Timestamp"].str.strip()

# Convert 'Timestamp' column to datetime format using dateutil.parser.parse
df["Timestamp"] = df["Timestamp"].apply(lambda x: parse(x, dayfirst=True))

# Debug: Print rows with NaT in 'Timestamp' to identify parsing issues
print("Rows with NaT in 'Timestamp':")
print(df[df["Timestamp"].isna()])

# Remove rows with missing values in key columns
df.dropna(subset=["Case_ID", "Activity", "Timestamp"], inplace=True)

# Ensure string types for key columns
df["Case_ID"] = df["Case_ID"].astype("string")
df["Activity"] = df["Activity"].astype("string")

# Ensure the data is sorted by Case_ID and Timestamp
df.sort_values(by=["Case_ID", "Timestamp"], inplace=True)

# Debug: Print the sorted dataframe to verify the order
print("Sorted DataFrame:")
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