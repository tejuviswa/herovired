import requests
from datetime import datetime, timedelta

# actual GitHub username and personal access token
username = "tejuviswa"
access_token = "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"

# Specify repository owner and name if checking a specific repo
repo_owner = "tejuviswa"  # Default is your own repositories
repo_name = "herovired"

# URL template for accessing commits endpoint
commits_url = f"https://api.github.com/repos/tejuviswa/herovired/commits"

# Last checked commit SHA (store in persistent storage for subsequent runs)
last_checked_commit = None
try:
    with open("last_checked_commit.txt", "r") as f:
        last_checked_commit = f.read().strip()
except FileNotFoundError:
    pass

# Authentication headers
headers = {"Authorization": f"token {access_token}"}

# Parameters for filtering commits
params = {
    "sha": last_checked_commit,  # Only return commits newer than the last checked one
    "per_page": 100,  # Retrieve a maximum of 100 commits at a time (paginating if necessary)
}

def check_for_new_commits():
    """
    Fetches new commits from the GitHub API and prints information about them.
    """

    global last_checked_commit

    while True:
        response = requests.get(commits_url, headers=headers, params=params)
        response.raise_for_status()  # Raise an exception for non-200 status codes

        commits = response.json()

        # If no new commits found, break the loop
        if not commits:
            break

        for commit in commits:
            commit_sha = commit["sha"]
            commit_message = commit["commit"]["message"]
            commit_date = datetime.strptime(commit["commit"]["committer"]["date"], "%Y-%m-%dT%H:%M:%SZ")


            print(f"New commit: {commit_sha} - {commit_message} (committed on {commit_date})")

            # Update last checked commit SHA for subsequent runs
            last_checked_commit = commit_sha

        # If there are more commits, update params for pagination
        next_page_url = response.links.get("next", None)
        if next_page_url:
            params["page"] = next_page_url.split("=")[1]
        else:
            break

    # Store the last checked commit SHA for next time
    with open("last_checked_commit.txt", "w") as f:
        f.write(last_checked_commit)

def trigger_deployment():
    subprocess.run(["./deploy.sh"])

# ... (code that checks for new commits)

# Assuming new_commits_found is calculated or set somewhere above this point in your code
new_commits_found = check_for_new_commits()

if new_commits_found:
    print("New commits found! Triggering deployment...")
    trigger_deployment()
else:
    print("No new commits found.")







if __name__ == "__main__":
    check_for_new_commits()
# ... (code that checks for new commits)



