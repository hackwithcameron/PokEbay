from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import CardSet, Card

class Index(View):

    def get(self, request):
        card = get_object_or_404(Card, number=1)

        context = {
            'card': card,
        }

        return render(request, 'Card/index.html', context)
