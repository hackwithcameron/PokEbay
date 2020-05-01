from pokemontcgsdk import Set, Card
import csv


class PokedexAPI:
    def __init__(self):
        self.url = 'https://api.pokemontcg.io/v1/cards'
        self.cardSetList = []
        self.setDict = {}
        self.headers = ['id', 'name', 'series', 'set', 'number', 'image_url', 'image_url_hi_res',
                        'subtype', 'supertype', 'ability', 'ancient_trait', 'hp', 'artist',
                        'rarity', 'set_code', 'retreat_cost', 'converted_retreat_cost', 'national_pokedex_number',
                        'text', 'types', 'attacks', 'weaknesses', 'resistances', 'evolves_from']
        self.getAllSetIds()

    def getCard(self, cardSet, cardNum):
        """
        :param cardSet: Name of the set the card is in
        :param cardNum: number of the card in the set
        :return: Card object with all card attributes
        """
        return Card.find(id=f"{self.setDict[cardSet].lower()}-{str(cardNum)}")

    def getCards(self, cardSet, cardNumStart, cardNumEnd):
        """
        Gets all card information from range of cards in card set
        :param cardSet: Name of set cards belongs to
        :param cardNumStart: Number of card to start with
        :param cardNumEnd: Number of card to end with
        :return: List of cards in set with card numbers between cardNumStart and cardNum End
        """
        return [self.getCard(cardSet.lower(), f'{x}') for x in range(cardNumStart, cardNumEnd + 1)]

    def getSet(self, setName):
        return Set.find(id=f"{self.setDict[setName].lower()}")

    def getAllSetIds(self):
        """
        Gets all card set names and corresponding codes
        :return: Prints list of sets to console
        """
        allCardSets = Set.all()
        cardSetName = [sets.name for sets in allCardSets]
        cardSetCode = [sets.code for sets in allCardSets]
        self.setDict = {cardSetName[i].lower(): cardSetCode[i] for i in range(len(cardSetName))}


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
