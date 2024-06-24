import requests


class GitLabService:
    BASE_URL = 'https://gitlab.com/api/v4'

    def get_repos(self, user):
        response = requests.get(f'{self.BASE_URL}/users/{user}/projects')
        return response.json()
