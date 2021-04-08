from star_wars_api.api_settings import Settings

import requests


def test_settings():
    response = requests.get(Settings().BASE_URL)
    assert response.status_code == 200
