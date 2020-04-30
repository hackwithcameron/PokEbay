import django
import datetime
import os
import time

def populate():
    start = time.time()
    pokedexAPI = PokedexAPI()
    end = time.time()
    print(f'pokedexAPI time: {end - start}')
    start = time.time()
    base = pokedexAPI.getSet('base')
    end = time.time()
    print(f'Get Set time: {end - start}')
    start = time.time()
    baseCardSet = addSet(name=base.name,
                         code=base.code,
                         ptcgo_code=base.ptcgo_code,
                         series=base.series,
                         total_cards=base.total_cards,
                         release_date=datetime.datetime.strptime(base.release_date, "%d/%m/%Y").strftime("%Y-%m-%d"),
                         symbol_url=base.symbol_url,
                         logo_url=base.logo_url)

    end = time.time()
    print(f'Add set to Database time: {end - start}')
    start = time.time()

    # Range of card numbers to add to 'Base' set
    baseCards = pokedexAPI.getCards(base.name, 5, 69)
    end = time.time()
    print(f'Get cards time: {end - start}')
    start = time.time()
    for card in baseCards:
        addCard(name=card.name,
                national_pokedex_number=card.national_pokedex_number,
                image_url=card.image_url,
                image_url_hi_res=card.image_url_hi_res,
                subtype=card.subtype,
                supertype=card.supertype,
                hp=card.hp,
                number=card.number,
                artist=card.artist,
                rarity=card.rarity,
                series=card.series,
                card_set=baseCardSet,
                set_code=card.set_code,
                types=card.types,
                evolves_from=card.evolves_from)

    end = time.time()
    print(f'Add cards to Database total time: {end - start}')


def addCard(name, national_pokedex_number, image_url, image_url_hi_res,
            subtype, supertype, hp, number, artist, rarity, series,
            card_set, set_code, types, evolves_from):
    card = Card.cards.get_or_create(name=name, national_pokedex_number=national_pokedex_number)[0]
    card.image_url = image_url
    card.image_url_hi_res = image_url_hi_res
    card.subtype = subtype
    card.supertype = supertype
    card.hp = hp
    card.number = number
    card.artist = artist
    card.rarity = rarity
    card.series = series
    card.card_set = card_set
    card.set_code = set_code
    card.types = types
    card.evolves_from = evolves_from
    card.save()
    return card


def addSet(name, code, ptcgo_code, series, total_cards, release_date, symbol_url, logo_url):
    cardSet = CardSet.card_sets.get_or_create(name=name)[0]
    cardSet.code = code
    cardSet.ptcgo_code = ptcgo_code
    cardSet.series = series
    cardSet.total_cards = total_cards
    cardSet.release_date = release_date
    cardSet.symbol_url = symbol_url
    cardSet.logo_url = logo_url
    cardSet.save()
    return cardSet


if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pokEbay.settings.py')
    django.setup()
    from Card.models import Card, CardSet
    from Card.scripts.pokedexAPI import PokedexAPI
    print('Populating database with cards...')
    total_time = time.time()
    populate()
    end = time.time()
    print('Populate complete.')
    print(f'Total Time: {end - total_time}')
