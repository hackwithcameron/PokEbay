from django.shortcuts import render
from django.views import View
from .scripts.pokedexAPI import PokedexAPI




class Index(View):

    def get(self, request):
        pokedexAPI = PokedexAPI()
        # Creates deck of cards
        cards = [pokedexAPI.getCard('base1', f'{x}') for x in range(1, 17)]
        # Creates single card
        card = pokedexAPI.getCard('base2', '15')

        context = {
            'card': card,
            'cards': cards
        }

        return render(request, 'Card/index.html', context)
