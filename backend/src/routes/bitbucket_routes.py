from flask import Blueprint, request, jsonify

from src.services.bitbucket_service import BitbucketService

bitbucket_bp = Blueprint('bitbucket', __name__)
bitbucket_service = BitbucketService()


@bitbucket_bp.route('/repos', methods=['GET'])
def get_bitbucket_repos():
    user = request.args.get('user')
    repos = bitbucket_service.get_repos(user)
    return jsonify(repos)
