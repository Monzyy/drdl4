import requests

from drdl4.settings import MU_URL, MU_FRONT_PAGE


def get_program_cards(id, expanded=False):
    url = f'{MU_URL}/programcard/{id}'
    params = {'expanded': expanded, }
    r = requests.get(url, params=params)
    program_cards = r.json()
    return program_cards


def get_top_spots():
    r = requests.get(MU_FRONT_PAGE)
    data = r.json()
    top_program_cards = data.get('TopSpots')
    return top_program_cards

