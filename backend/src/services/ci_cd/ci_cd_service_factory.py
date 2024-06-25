# backend/src/services/ci_cd/ci_cd_factory.py

from src.services.ci_cd.github_actions_service import GitHubActionsService
from src.services.ci_cd.jenkins_service import JenkinsService
from src.services.ci_cd.circleci_service import CircleCIService


def get_ci_cd_service(service_name):
    if service_name == 'jenkins':
        return JenkinsService()
    elif service_name == 'github_actions':
        return GitHubActionsService()
    elif service_name == 'circleci':
        return CircleCIService()
    else:
        raise ValueError(f"Unsupported CI/CD service: {service_name}")
