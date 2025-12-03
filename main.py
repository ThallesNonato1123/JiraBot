import argparse
from JiraClient import jira_client
from GithubClient import GithubClient

def build_parser():
    parser = argparse.ArgumentParser(description="CLI para o JiraBot")
    parser.add_argument("-id", "--issue-id", required=True, help="ID da issue (ex: PVTE-4894)")
    return parser

if __name__ == "__main__":
    github_client =  GithubClient("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", "ThallesNonato1123", "TESTE-BITRISE", 2)
    jira_tasks = github_client.getJirasAssociatedTasks()
    for task in jira_tasks:
        jira_client.move_to_done(task)