from django.shortcuts import render
from django.views import View
from .scripts.cardScraper import CardScraper


class Index(View):

    def get(self, request):

        cardInfo = CardScraper('121')
        card = cardInfo.getData()
        context = {
            'card': card
        }

        return render(request, 'Card/index.html', context)
