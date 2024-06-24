from flask import Blueprint, request, jsonify

from src.services.gitlab_service import GitLabService

gitlab_bp = Blueprint('gitlab', __name__)
gitlab_service = GitLabService()


@gitlab_bp.route('/repos', methods=['GET'])
def get_gitlab_repos():
    user = request.args.get('user')
    repos = gitlab_service.get_repos(user)
    return jsonify(repos)
