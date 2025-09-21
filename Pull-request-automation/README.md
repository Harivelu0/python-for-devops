# 🚀 Pull Request Slack Notification Automation

This Python script automates the deployment of a GitHub Actions workflow to all repositories owned by a user. The workflow sends Slack notifications whenever a pull request is opened, reopened, synchronized, or marked ready for review.

## Features

- Validates required environment variables from a `.env` file
- Checks GitHub token validity
- Lists all repositories owned by the authenticated user
- Deploys or updates a workflow file in each repository to notify a Slack channel about pull request events

## Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- GitHub personal access token with `repo` scope
- Slack channel ID and workspace token
- `.env` file with the following variables:

```
GITHUB_TOKEN=your_personal_access_token
GITHUB_USERNAME=your_github_username
SLACK_CHANNEL_ID=your_slack_channel_id
```

## Installation

1. Clone this repository.
2. Install dependencies:

   ```
   pip install requests python-dotenv pyyaml
   ```

3. Create a `.env` file in the project directory and add your credentials.

## Usage

Run the script:

```
python pr-flow.py
```

- The script will validate your credentials, list your repositories, and prompt for confirmation before deploying the workflow.
- The workflow will be added/updated at `.github/workflows/pr-slack-notification.yml` in each repository.

## How It Works

- **GitHub API**: Used to list repositories and create/update workflow files.
- **Slack Notification**: The workflow uses [`slackapi/slack-github-action`](https://github.com/slackapi/slack-github-action) to send notifications to your Slack channel when a pull request event occurs.

## Customization

- You can modify the workflow content in `pr-flow.py` to customize the Slack message or supported events.

## Troubleshooting

- Ensure your GitHub token has the correct permissions.
- Make sure your Slack workspace token is configured as a GitHub secret named `SLACK_WORKSPACE_TOKEN` in each repository.
- If you encounter missing environment variables, update your `.env` file.

## License

MIT

---

Made with ❤️ by hari https://dev.to/techwithhari/automating-github-pr-notifications-with-slack-integration-a-journey-2mje