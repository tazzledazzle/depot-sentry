# backend/src/services/ci_cd/circleci_service.py
from .base_ci_cd import BaseCICDService


class CircleCIService(BaseCICDService):
    def trigger_build(self, repo_url):
        # Implement CircleCI build trigger logic
        pass

    def get_build_status(self, build_id):
        # Implement CircleCI build status logic
        pass

    def get_latest_builds(self, repo_url):
        # Implement CircleCI latest builds logic
        pass
