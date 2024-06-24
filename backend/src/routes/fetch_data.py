import requests


def fetch_github_repos(user):
    url = f"https://api.github.com/users/{user}/repos"
    response = requests.get(url)
    return response.json()
