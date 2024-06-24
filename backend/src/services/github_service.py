import requests


class GitHubService:
    BASE_URL = 'https://api.github.com'

    def get_repos(self, user):
        response = requests.get(f'{self.BASE_URL}/users/{user}/repos')
        return response.json()
