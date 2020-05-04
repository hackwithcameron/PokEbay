from django.contrib import admin
from .models import CardSet, Card


class Cards(admin.ModelAdmin):
    list_display = ('name', 'card_set', 'national_pokedex_number')


admin.site.register(CardSet)
admin.site.register(Card, Cards)
