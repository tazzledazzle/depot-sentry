# backend/src/tests/test_bitbucket_routes.py

def test_get_bitbucket_repos(client, mocker):
    # Mock the BitbucketService
    mock_bitbucket_service = mocker.patch('src.services.bitbucket_service.BitbucketService.get_repos')
    mock_bitbucket_service.return_value = [{'id': 1, 'name': 'repo1'}]

    # Make the request
    response = client.get('/bitbucket/repos', query_string={'user': 'testuser'})

    # Assert the response
    assert response.status_code == 200
    assert response.json == [{'id': 1, 'name': 'repo1'}]
