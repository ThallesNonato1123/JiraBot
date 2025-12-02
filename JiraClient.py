from jira import JIRA

class JiraClient:
    def __init__(self, server: str, email: str, api_token: str):
        self.jira = JIRA(
            server=server,
            basic_auth=(email, api_token)
        )

    def search_issues(self, jql: str, max_results: int = 50):
        """Busca issues usando JQL."""
        return self.jira.search_issues(jql, maxResults=max_results)

    def print_issues(self, issues):
        """Imprime chave, resumo e status de uma lista de issues."""
        for issue in issues:
            print(f"{issue.key}: {issue.fields.summary} ({issue.fields.status.name})")

    def get_issues_in_code_review(self, project_key: str):
        """Busca issues que estão no status 'In Code Review [T_DCT]'."""
        jql = f'project = {project_key} AND status = "In Code Review [T_DCT]"'
        return self.search_issues(jql, max_results=100)
    
    def get_jira_transitions(self, id):
        transitions = jira_client.jira.transitions(id)
        for t in transitions:
            print(f"{t['id']} - {t['name']}")
    
    def move_to_ready_to_release(self,id):
        self.jira.transition_issue(id, "561")

    def move_to_done(self,id):
        self.jira.transition_issue(id, "571")
    
    def print_all_issues(self, project_key: str):
        issues = self.jira.search_issues(f'project = {project_key}', maxResults=1000)
        for issue in issues:
            print(f"{issue.key} - {issue.fields.summary}- ({issue.fields.status.name})")


jira_client = JiraClient(
    server="https://globo.atlassian.net",
    email="thalles.nonato@g.globo",
    api_token="ATATT3xFfGF0ggSDMW7r7WhLO7GlZYD-a0O5Y3ud7UM2KohUfVDIDkya_gvbPC4U2fKKsGABGVwL8AXF90d9MwJ6GneV7LfNRJXLsC7P0uwVhwrlrwtefZ-p3aiQsJHPL0OFaNPmKnAf2RJhlpzltHCZsfNu4FuJo8--r2MUFTr-GXCABrjy5VU=6968F166"
)
