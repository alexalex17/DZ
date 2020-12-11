import urllib.parse as urllib

def parse_parameters(query: str) -> dict:
    url=query
    d = url.split('/?')[0]
    d = urllib.urlparse(url)
    qd = dict(urllib.parse_qsl(d.query))
    return qd


def parse_cookies(query: str) -> dict:
    return {}


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
