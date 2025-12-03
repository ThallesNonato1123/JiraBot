from JiraClient import jira_client
from GithubClient import GithubClient
import os
import sys

if __name__ == "__main__":
    github_token = os.getenv("GITHUB_TEST")
    pr_number = os.getenv("BITRISE_PULL_REQUEST")
    if pr_number:
        print(f"PR Number: {pr_number}")
    else:
        print("Nenhum PR detectado (variável vazia).")
        sys.exit(1)

    github_client =  GithubClient(github_token, "ThallesNonato1123", "TESTE-BITRISE", int(pr_number))
    jira_tasks = github_client.getJirasAssociatedTasks()
    for task in jira_tasks:
        print(task)
        jira_client.move_to_done(task)