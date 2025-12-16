from JiraClient import jira_client
from GithubClient import GithubClient
import sys
import re

def get_version_name(device: str):
    
    if( device == "android"):
        with open("../app/build.gradle", "r", encoding="utf-8") as f:
            for line in f:
                if "versionName" in line:
                    match = re.search(r'"([^"]+)"', line)
                    if match:
                        return match.group(1)
    
    elif (device == "ios"):
        with open("../xcodegen/settings.yml") as f:
            for line in f:
                if "&version" in line:
                    match = re.search(r'"([^"]+)"', line)
                    if match:
                        return match.group(1)

def create_jira_version():
    jira_client.create_version("PTVE", "Android" )

if __name__ == "__main__":
    github_token = ""
    merged_prs = sys.stdin.readlines()
    
    prs = []
    
    for pr_merge in merged_prs:
        refs = re.findall(r"#(\d+)", pr_merge)
        refs = list(map(int, refs))
        prs.append(refs[0])

    github_client =  GithubClient(github_token, "globoi", "premiere-play-android")
    versionName = get_version_name("android")
    versionName = "1.0.0"
    jiraVersion = jira_client.create_version(f"Premiere Android v{versionName}", "PTVE")

    for pr in prs:
        taskCode = github_client.getJiraTaskCode(pr)
        jira_client.add_tasks_to_version(taskCode, jiraVersion.id, jiraVersion.name)

    ### primeiro colocar os cards na release (jira) (pr de release aberto)
    ## mover os cards para done (pr de release fechado)