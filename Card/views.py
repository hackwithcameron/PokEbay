from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView
from .models import CardSet, Card


class Index(ListView):
    model = Card
    context_object_name = 'cards'
    queryset = Card.cards.all()
    paginate_by = 10
    template_name = 'Card/index.html'

#    def get(self, request):
#        card = get_object_or_404(Card, number=15)
#
#        context = {
#            'card': card,
#        }
#
#        return render(request, 'Card/index.html', context)
