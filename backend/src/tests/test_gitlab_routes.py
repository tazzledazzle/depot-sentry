# backend/src/tests/test_gitlab_routes.py

def test_get_gitlab_repos(client, mocker):
    # Mock the GitLabService
    mock_gitlab_service = mocker.patch('src.services.gitlab_service.GitLabService.get_repos')
    mock_gitlab_service.return_value = [{'id': 1, 'name': 'repo1'}]

    # Make the request
    response = client.get('/gitlab/repos', query_string={'user': 'testuser'})

    # Assert the response
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'name': 'repo1'}]
