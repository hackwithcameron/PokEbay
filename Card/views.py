from django.shortcuts import render
from django.views import View
from .scripts.pokedexAPI import PokedexAPI




class Index(View):

    def get(self, request):
        pokedexAPI = PokedexAPI()
        card = pokedexAPI.getCard('base', 15)



        context = {
            'card': card,
        }

        return render(request, 'Card/index.html', context)
