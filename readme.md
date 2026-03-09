# Empirical Investigation of the Effect of Modularity on Failure Rates in Python Software Systems

## Overview

This project investigates whether software modularity influences the frequency of failures in Python software systems. The study analyzes a dataset of open-source Python repositories mined from GitHub. Structural modularity metrics are extracted from source code, and failure rates are estimated from version control history using commit messages related to bug fixes.

The goal of this research is to determine whether modular design characteristics correlate with lower failure rates in Python projects.

---

## Research Method

The study follows an empirical quantitative methodology using repository mining techniques.

1. Python repositories are collected from GitHub.
2. Structural modularity metrics are extracted from source code.
3. Failure frequency is estimated using commit history and bug-fix commits.
4. The collected dataset is analyzed using statistical methods to evaluate the relationship between modularity and failure rates.

---

## Dataset

The dataset contains metrics collected from multiple open-source Python repositories.

Collected attributes include:

* Module count
* Import dependency count
* Dependency density
* Total number of commits
* Number of bug-fix commits
* Failure rate

The dataset files are located in the `dataset/` directory.

---

## Tools and Libraries

The project uses the following tools and Python libraries:

* Python
* PyDriller (repository mining)
* pandas (data processing)
* SciPy (statistical analysis)
* matplotlib (visualization)

---

## Repository Structure

```
python-modularity-failure-study
│
├ dataset
│   modularity_metrics.csv
│   failure_data.csv
│   final_dataset.csv
│
├ scripts
│   modularity_metrics.py
│   failure_analysis.py
│   merge_dataset.py
│   statistical_analysis.py
│
├ results
│   modularity_failure_graph.png
│
└ README.md
```

---

## How to Reproduce the Study

1. Clone the repositories used for analysis.
2. Run the modularity metric extraction script:

```
python scripts/modularity_metrics.py
```

3. Run the failure analysis script:

```
python scripts/failure_analysis.py
```

4. Merge the collected datasets:

```
python scripts/merge_dataset.py
```

5. Perform statistical analysis and generate the visualization:

```
python scripts/statistical_analysis.py
```

---

## Results

The relationship between modularity and failure rate is visualized using a scatter plot generated from the analyzed dataset.

The resulting graph is located in:

```
results/modularity_failure_graph.png