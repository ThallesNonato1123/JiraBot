from github import Github
import re

class GithubClient:
    def __init__(self, token, owner, repoName) -> None:
        self.github = Github(token)
        self.repo = self.github.get_repo(f"{owner}/{repoName}")
    
    def getPullRequest(self, pr_number=None):
        """Busca o PR, baseado em um id."""
        return self.repo.get_pull(pr_number)
    
    def getAssociatedPrs(self):
        """Busca os PRs que foram associados a esse PR."""
        pr = self.getPullRequest()
        refs = re.findall(r"#(\d+)", pr.body)
        refs = list(map(int, refs))
        set_refs = set()
        for ref in refs:
            set_refs.add(ref)
        return list(set_refs)
    
    def getJirasAssociatedTasks(self):
        """Busca as Tasks do Jira associadas a um PR."""
        tasks_list = []
        for numberPr in self.getAssociatedPrs():
            prName = self.getPullRequest(numberPr).head.ref
            task = prName.rsplit("/", 1)[-1]
            tasks_list.append(task)
        return tasks_list
    
    
    def getJiraTaskCode(self, prNumber):
        prName = self.getPullRequest(prNumber).head.ref
        task = prName.rsplit("/", 1)[-1]
        return task

    
    def getReleases(self):
        releases = self.repo.get_releases()
        return releases