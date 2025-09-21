import requests
import base64
import yaml
import os
import sys
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Environment variables configuration
REQUIRED_ENV_VARS = {
    'GITHUB_TOKEN': os.getenv('GITHUB_TOKEN'),
    'GITHUB_USERNAME': os.getenv('GITHUB_USERNAME'),
    'SLACK_CHANNEL_ID': os.getenv('SLACK_CHANNEL_ID')
}

# Validate environment variables
missing_vars = [var for var, value in REQUIRED_ENV_VARS.items() if not value]
if missing_vars:
    print("Error: Missing required environment variables:")
    for var in missing_vars:
        print(f"- {var}")
    print("\nPlease add them to your .env file:")
    print("""
    GITHUB_TOKEN=your_personal_access_token
    GITHUB_USERNAME=your_github_username
    SLACK_CHANNEL_ID=your_slack_channel_id
    """)
    sys.exit(1)

# GitHub API headers
HEADERS = {
    "Authorization": f"token {REQUIRED_ENV_VARS['GITHUB_TOKEN']}",
    "Accept": "application/vnd.github.v3+json"
}

# Workflow content with environment variables
workflow_content = f"""
name: PR Slack Notification

on:
  pull_request:
    types: [opened, reopened, synchronize, ready_for_review]
    branches:
      - main
      - master
      - develop

jobs:
  notify-slack:
    runs-on: ubuntu-latest
    steps:
      - name: Send Slack notification
        uses: slackapi/slack-github-action@v1.24.0
        with:
          channel-id: '{REQUIRED_ENV_VARS["SLACK_CHANNEL_ID"]}'
          slack-message: |
            🔔 New Pull Request in *${{{{ github.repository }}}}*
            
            *Title:* ${{{{ github.event.pull_request.title }}}}
            *Author:* ${{{{ github.event.pull_request.user.login }}}}
            *Branch:* ${{{{ github.event.pull_request.head.ref }}}}
            *Repository:* ${{{{ github.repository }}}}
            
            👉 <${{{{ github.event.pull_request.html_url }}}}|View Pull Request>
            
            *Description:*
            ${{{{ github.event.pull_request.body || 'No description provided.' }}}}
        env:
          SLACK_TOKEN: ${{{{ secrets.SLACK_WORKSPACE_TOKEN }}}}
"""

def test_github_connection():
    """Test GitHub API connection and token validity"""
    url = "https://api.github.com/user"
    response = requests.get(url, headers=HEADERS)
    if response.status_code != 200:
        print(f"Error: GitHub token validation failed (Status code: {response.status_code})")
        print("Please check your GITHUB_TOKEN")
        sys.exit(1)
    print("✅ GitHub token validated successfully")
    return response.json()["login"]

def get_user_repos():
    """Get all repositories for the user"""
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/user/repos?affiliation=owner&per_page=100&page={page}"
        response = requests.get(url, headers=HEADERS)
        if response.status_code != 200:
            print(f"Error getting repositories: {response.status_code}")
            print(f"Error message: {response.text}")
            return []
        
        page_repos = response.json()
        if not page_repos:
            break
            
        repos.extend(page_repos)
        page += 1
    
    return repos

def create_workflow_file(repo_name):
    """Create or update the workflow file in a repository"""
    encoded_content = base64.b64encode(workflow_content.encode()).decode()
    
    workflow_path = ".github/workflows/pr-slack-notification.yml"
    url = f"https://api.github.com/repos/{REQUIRED_ENV_VARS['GITHUB_USERNAME']}/{repo_name}/contents/{workflow_path}"
    response = requests.get(url, headers=HEADERS)
    
    if response.status_code == 404:
        data = {
            "message": "Add PR Slack notification workflow",
            "content": encoded_content,
            "branch": "main"
        }
    else:
        existing_file = response.json()
        data = {
            "message": "Update PR Slack notification workflow",
            "content": encoded_content,
            "sha": existing_file["sha"],
            "branch": "main"
        }
    
    response = requests.put(url, headers=HEADERS, json=data)
    return response.status_code == 200 or response.status_code == 201

def main():
    # Validate GitHub token and get authenticated username
    authenticated_user = test_github_connection()
    if authenticated_user.lower() != REQUIRED_ENV_VARS['GITHUB_USERNAME'].lower():
        print(f"Warning: Authenticated user ({authenticated_user}) doesn't match GITHUB_USERNAME ({REQUIRED_ENV_VARS['GITHUB_USERNAME']})")
        confirm = input("Do you want to continue? (y/N): ")
        if confirm.lower() != 'y':
            sys.exit(1)

    print(f"\nFetching repositories for user {REQUIRED_ENV_VARS['GITHUB_USERNAME']}...")
    repos = get_user_repos()
    print(f"Found {len(repos)} repositories")
    
    if not repos:
        print("No repositories found. Please check your permissions and try again.")
        sys.exit(1)

    # Show summary before proceeding
    print("\nReady to deploy workflow to the following repositories:")
    for repo in repos:
        print(f"- {repo['name']} ({'private' if repo['private'] else 'public'})")
    
    confirm = input("\nDo you want to proceed with the deployment? (y/N): ")
    if confirm.lower() != 'y':
        print("Deployment cancelled.")
        sys.exit(0)

    # Deploy workflows
    success_count = 0
    for repo in repos:
        repo_name = repo["name"]
        repo_type = "private" if repo["private"] else "public"
        print(f"\nProcessing {repo_name} ({repo_type})...")
        
        if create_workflow_file(repo_name):
            print(f"✅ Successfully deployed workflow to {repo_name}")
            success_count += 1
        else:
            print(f"❌ Failed to deploy workflow to {repo_name}")

    # Print summary
    print(f"\nDeployment completed: {success_count}/{len(repos)} successful")

if __name__ == "__main__":
    main()