# backend/src/services/ci_cd/base_ci_cd.py
class BaseCICDService:
    def trigger_build(self, repo_url):
        raise NotImplementedError

    def get_build_status(self, build_id):
        raise NotImplementedError

    def get_latest_builds(self, repo_url):
        raise NotImplementedError
