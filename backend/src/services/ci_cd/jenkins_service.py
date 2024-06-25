# backend/src/services/ci_cd/jenkins_service.py
from .base_ci_cd import BaseCICDService


class JenkinsService(BaseCICDService):
    def trigger_build(self, repo_url):
        # Implement Jenkins build trigger logic
        pass

    def get_build_status(self, build_id):
        # Implement Jenkins build status logic
        pass

    def get_latest_builds(self, repo_url):
        # Implement Jenkins latest builds logic
        pass
