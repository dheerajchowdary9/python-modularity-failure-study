import os
import csv
from pydriller import Repository

keywords = ["fix","bug","error","issue","defect"]

repo_base = "repositories"

results = []

for repo in os.listdir(repo_base):

    repo_path = os.path.join(repo_base, repo)

    if not os.path.isdir(repo_path):
        continue

    total_commits = 0
    bug_commits = 0

    for commit in Repository(repo_path).traverse_commits():

        total_commits += 1

        msg = commit.msg.lower()

        if any(word in msg for word in keywords):

            bug_commits += 1

    failure_rate = bug_commits / total_commits if total_commits else 0

    results.append([repo,total_commits,bug_commits,failure_rate])

with open("dataset/failure_data.csv","w",newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "repo",
        "total_commits",
        "bug_commits",
        "failure_rate"
    ])

    writer.writerows(results)

print("Failure data collected.")