import requests


def buscar_avatar(usuario):
    """
    Busca o avatar do usuario
    :param usuario: str nome do avatar do github
    :return: str link do avatar do usuario
    """
    url = f'https://api.github.com/users/{usuario}'
    resp = requests.get(url)
    return resp.json()['avatar_url']


if __name__ == '__main__':
    print(buscar_avatar('89lucasrosa'))
