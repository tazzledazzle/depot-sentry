from flask import Blueprint, request, jsonify

from src.services.github_service import GitHubService

github_bp = Blueprint('github', __name__)
github_service = GitHubService()


@github_bp.route('/repos', methods=['GET'])
def get_github_repos():
    user = request.args.get('user')
    repos = github_service.get_repos(user)
    return jsonify(repos)
