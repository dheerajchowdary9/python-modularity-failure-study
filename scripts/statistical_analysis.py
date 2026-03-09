import pandas as pd
from scipy.stats import pearsonr
import matplotlib.pyplot as plt

df = pd.read_csv("dataset/final_dataset.csv")

corr, p = pearsonr(df["dependency_density"], df["failure_rate"])

print("Correlation:",corr)
print("P value:",p)

plt.scatter(df["dependency_density"], df["failure_rate"])

plt.xlabel("Dependency Density")
plt.ylabel("Failure Rate")

plt.title("Modularity vs Failure Rate")

plt.savefig("results/modularity_failure_graph.png")

plt.show()