import argparse
from JiraClient import jira_client

def build_parser():
    parser = argparse.ArgumentParser(description="CLI para o JiraBot")
    parser.add_argument("-id", "--issue-id", required=True, help="ID da issue (ex: PVTE-4894)")
    return parser

if __name__ == "__main__":
    parser = build_parser()
    args = parser.parse_args()

    issue_id = args.issue_id
    print("Issue informada:", issue_id)

    jira = jira_client
    jira.move_to_done(issue_id)