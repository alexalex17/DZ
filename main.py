import urllib.parse as urllib

def parse_parameters(query: str) -> dict:
    url=query
    d = url.split('/?')[0]
    d = urllib.urlparse(url)
    qd = dict(urllib.parse_qsl(d.query))
    return qd


def parse_cookies(query: str) -> dict:
    S=query
    D=dict(i.split('=') for i in S.replace(';', '').split())
    return D


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse_parameters('https://www.google.com.ua/?hl=ru') == {'hl': 'ru'}
    assert parse_parameters('https://rozetka.com.ua/search/?text=samsung+a51&producer=12') == {'text': 'samsung a51', 'producer': '12'}
    assert parse_parameters('https://rozetka.com.ua/search/?text=ddr3') == {'text': 'ddr3'}
    assert parse_parameters('https://allo.ua/ru/catalogsearch/result/?q=samsung') == {'q': 'samsung'}
    assert parse_parameters('https://www.google.com/search?q=%D0%B2%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F&rlz=1C1CHBD_ruUA917UA917&oq=%D0%B2%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F&aqs=chrome..69i57j0j0i433j0j69i65l2j69i61l2.2103j0j4&sourceid=chrome&ie=UTF-8') == {'q': 'википедия', 'rlz': '1C1CHBD_ruUA917UA917', 'oq': 'википедия', 'aqs': 'chrome..69i57j0j0i433j0j69i65l2j69i61l2.2103j0j4', 'sourceid': 'chrome', 'ie': 'UTF-8'}
    assert parse_parameters('https://www.youtube.com/watch?v=VrXK4Qk60Fo&ab_channel=NSKShow.') == {'v': 'VrXK4Qk60Fo', 'ab_channel': 'NSKShow.'}
    assert parse_parameters('https://www.youtube.com/?gl=UA&hl=ru') == {'gl': 'UA', 'hl': 'ru'}
    assert parse_parameters('https://developer.mozilla.org/ru/search?q=URL') =={'q': 'URL'}
    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
