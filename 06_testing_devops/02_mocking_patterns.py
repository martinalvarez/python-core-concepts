from unittest.mock import patch
import requests

def get_external_status(url: str):
    response = requests.get(url)
    return response.status_code

def test_get_status_with_mock():
    # We 'patch' the requests.get so it doesn't actually call the internet
    with patch('requests.get') as mocked_get:
        # We define what the mock should return
        mocked_get.return_value.status_code = 200
        
        status = get_external_status("https://fake-api.com")
        
        assert status == 200
        mocked_get.assert_called_once_with("https://fake-api.com")