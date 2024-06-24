import requests


class BitbucketService:
    BASE_URL = 'https://api.bitbucket.org/2.0'

    def get_repos(self, user):
        response = requests.get(f'{self.BASE_URL}/repositories/{user}')
        return response.json()
