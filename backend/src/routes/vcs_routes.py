from flask import Blueprint, request, jsonify

from src.services.github_service import GitHubService
from src.services.bitbucket_service import BitbucketService
from src.services.gitlab_service import GitLabService

vcs_bp = Blueprint('vcs', __name__)


@vcs_bp.route('/repos', methods=['GET'])
def get_all_repos():
    user = request.args.get('user')
    github_repos = GitHubService().get_repos(user)
    gitlab_repos = GitLabService().get_repos(user)
    bitbucket_repos = BitbucketService().get_repos(user)
    all_repos = github_repos + gitlab_repos + bitbucket_repos
    return jsonify(all_repos)

#
# @app.route('/api/repos', methods=['GET'])
# def get_repos():
#     # Logic to fetch repository data
#     return jsonify({"message": "Repository data"}), 200
