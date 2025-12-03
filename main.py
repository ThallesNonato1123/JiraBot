from JiraClient import jira_client
from GithubClient import GithubClient
import os

if __name__ == "__main__":
    github_token = os.getenv("GITHUB_TEST")
    github_client =  GithubClient(github_token, "ThallesNonato1123", "TESTE-BITRISE", 2)
    jira_tasks = github_client.getJirasAssociatedTasks()
    for task in jira_tasks:
        print(task)
        jira_client.move_to_done(task)