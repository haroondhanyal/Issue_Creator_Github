import requests


# Step 1: Get blueprints with ID of 3 from DevLake API
devlake_api_url = "http://54.236.25.78:4000/api/v1/blueprints/3"
response = requests.get(devlake_api_url)
print(response.status_code)
print(response.text)

if response.status_code == 200:
    blueprint_data = response.json()
else:
    print(f"Error retrieving data from DevLake API. Status code: {response.status_code}")
    print(response.text)
    exit()

# Step 2: Extract the name of one GitLab repository from the blueprint data
if "repositories" in blueprint_data and blueprint_data["repositories"]:
    gitlab_repo_name = blueprint_data["repositories"][0]["name"]
else:
    print("No GitLab repository found in the blueprint data.")
    exit()

# Step 3: Manually create a GitHub repo and get the necessary credentials
github_username = "haroondhanyal"
github_token = "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"
github_repo_name = "github_issue_creator"

# Step 4: Use GitHub API to create a new issue
github_api_url = f"https://api.github.com/repos/{github_username}/{github_repo_name}/issues"
issue_title = f"New Issue for {gitlab_repo_name}"
issue_body = "An issue is created through GitHUb API."

headers = {
    "Authorization": f"token {github_token}",
    "Accept": "application/vnd.github.v3+json"
}

issue_data = {
    "title": issue_title,
    "body": issue_body
}

response = requests.post(github_api_url, headers=headers, json=issue_data)

if response.status_code == 201:
    print(f"New issue created successfully on GitHub. Issue Title: {issue_title}")
else:
    print(f"Error creating issue on GitHub. Status code: {response.status_code}")
    print(response.text)
