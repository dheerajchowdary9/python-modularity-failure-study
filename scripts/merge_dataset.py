import pandas as pd

mod = pd.read_csv("dataset/modularity_metrics.csv")
fail = pd.read_csv("dataset/failure_data.csv")

merged = pd.merge(mod, fail, on="repo")

merged.to_csv("dataset/final_dataset.csv",index=False)

print("Dataset merged.")