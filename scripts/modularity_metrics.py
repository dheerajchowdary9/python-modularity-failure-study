import os
import csv
import re

repo_base = "repositories"

results = []

for repo in os.listdir(repo_base):

    repo_path = os.path.join(repo_base, repo)

    if not os.path.isdir(repo_path):
        continue

    module_count = 0
    import_count = 0

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                module_count += 1

                path = os.path.join(root, file)

                try:
                    with open(path, "r", encoding="utf8", errors="ignore") as f:
                        code = f.read()
                        imports = re.findall(r"import ", code)
                        import_count += len(imports)
                except:
                    pass

    dependency_density = import_count / module_count if module_count else 0

    results.append([repo, module_count, import_count, dependency_density])

with open("dataset/modularity_metrics.csv","w",newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "repo",
        "module_count",
        "import_count",
        "dependency_density"
    ])

    writer.writerows(results)

print("Modularity metrics collected.")