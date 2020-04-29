from pokemontcgsdk import Set, Card
import csv


class PokedexAPI:
    def __init__(self):
        self.url = 'https://api.pokemontcg.io/v1/cards'
        self.allCardSets = Set.all()
        self.cardSetList = []
        self.cardSetName = [sets.__getattribute__('name') for sets in self.allCardSets]
        self.cardSetCode = [sets.__getattribute__('code') for sets in self.allCardSets]
        self.headers = ['id', 'name', 'series', 'set', 'number', 'image_url', 'image_url_hi_res',
                        'subtype', 'supertype', 'ability', 'ancient_trait', 'hp', 'artist',
                        'rarity', 'set_code', 'retreat_cost', 'converted_retreat_cost', 'national_pokedex_number',
                        'text', 'types', 'attacks', 'weaknesses', 'resistances', 'evolves_from']

    def getCard(self, cardSet, cardNum):
        """

        :param cardSet:
        :param cardNum:
        :return:
        """
        card = Card.find(id=f"{cardSet}-{cardNum}")
        return card

    def getAllSetIds(self):
        """
        Gets all card set names and corresponding codes
        :return: Prints list of sets to console
        """
        for i in range(len(self.cardSetName)):
            self.cardSetList.append(f"Name: {self.cardSetName[i]}, Code: {self.cardSetCode[i]}")
        for index in range(len(self.cardSetList)):
            print(self.cardSetList[index])

    def createCardCSV(self, cardSet, cardNum):
        """
        Creates .csv for any card searched
        :param cardSet: Set code for which the card belongs
        :param cardNum: Card number in set
        :return: CSV with card info name of csv is pokemon name
        """
        card = self.getCard(cardSet, cardNum)
        cardDetails = [card.__getattribute__(x) for x in self.headers]
        cardDict = {self.headers[i]: cardDetails[i] for i in range(len(self.headers))}
        with open(f'{card.name}.csv', mode='w') as csvFile:
            fieldnames = self.headers
            pokemonWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            pokemonWriter.writeheader()
            pokemonWriter.writerow(cardDict)
