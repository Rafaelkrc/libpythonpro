from unittest.mock import Mock

from libpythonpro import github_api


def test_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'Rafaelkrc', 'id': 87201775,
        'avatar_url': 'https://avatars.githubusercontent.com/u/87201775?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('rafaelkrc')
    assert 'https://avatars.githubusercontent.com/u/87201775?v=4' == url
