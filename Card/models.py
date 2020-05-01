from django.db import models


class CardSet(models.Model):
    code = models.CharField(max_length=20)
    ptcgo_code = models.CharField(max_length=20)
    name = models.CharField(max_length=25)
    series = models.CharField(max_length=25)
    total_cards = models.IntegerField(null=True)
    release_date = models.DateField(null=True)
    symbol_url = models.URLField()
    logo_url = models.URLField()

    card_sets = models.Manager()

    def __str__(self):
        return self.name


class Card(models.Model):
    name = models.CharField(max_length=50)
    national_pokedex_number = models.IntegerField(null=True)
    image_url = models.URLField()
    image_url_hi_res = models.URLField()
    subtype = models.CharField(max_length=50)
    supertype = models.CharField(max_length=50)
    hp = models.CharField(max_length=10)
    number = models.CharField(max_length=10)
    artist = models.CharField(max_length=50)
    rarity = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    card_set = models.ForeignKey(CardSet, on_delete=models.SET_NULL, null=True)
    set_code = models.CharField(max_length=50)
    types = models.CharField(max_length=20)
    evolves_from = models.CharField(max_length=50, null=True)

    cards = models.Manager()

    def __str__(self):
        return self.name
