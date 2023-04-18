import requests


def the_most_intlg_hero(hero1, hero2, hero3):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    resp = requests.get(url)
    data = resp.json()
    intelligence_list = []
    heroes_list = []

    for hero in data:
        if hero['name'] == hero1 or hero['name'] == hero2 or hero['name'] == hero3:
            intelligence_list.append(hero['powerstats']['intelligence'])
            heroes_list.append(hero['name'])

    max_intelligence = max(list(zip(intelligence_list, heroes_list)))
    print(f'The most intelligent hero is {max_intelligence[1]}.')
    return


if __name__ == '__main__':
    the_most_intlg_hero('Hulk', 'Captain America', 'Thanos')
