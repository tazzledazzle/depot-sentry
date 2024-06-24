# backend/src/tests/test_vcs_routes.py

def test_testfixure():
    assert True


def test_get_all_repos(client, mocker):
    # Mock the GitHubService, GitLabService, and BitbucketService
    mock_github_service = mocker.patch('src.services.github_service.GitHubService.get_repos')
    mock_gitlab_service = mocker.patch('src.services.gitlab_service.GitLabService.get_repos')
    mock_bitbucket_service = mocker.patch('src.services.bitbucket_service.BitbucketService.get_repos')

    mock_github_service.return_value = [{'id': 1, 'name': 'repo1'}]
    mock_gitlab_service.return_value = [{'id': 2, 'name': 'repo2'}]
    mock_bitbucket_service.return_value = [{'id': 3, 'name': 'repo3'}]

    # Make the request
    response = client.get('/vcs/repos', query_string={'user': 'testuser'})

    # Assert the response
    assert response.status_code == 200
    assert response.json == [
        {'id': 1, 'name': 'repo1'},
        {'id': 2, 'name': 'repo2'},
        {'id': 3, 'name': 'repo3'}
    ]
