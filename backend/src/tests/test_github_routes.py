# backend/src/tests/test_github_routes.py


def test_get_github_repos(client, mocker):
    # Mock the GitHubService
    mock_github_service = mocker.patch('src.services.github_service.GitHubService.get_repos')
    mock_github_service.return_value = [{'id': 1, 'name': 'repo1'}]

    # Make the request
    response = client.get('/github/repos', query_string={'user': 'testuser'})

    # Assert the response
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'name': 'repo1'}]
