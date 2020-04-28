from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
import csv

class CardScraper:

    def __init__(self, urlTag):
        url = requests.get('https://www.pocketmonsters.net/tcg/card/' + urlTag)
        soup = bs(url.content, 'html.parser')
        cardBody = soup.find(id="cardBody")
        self.table = cardBody.find('table')
        self.cardImg = soup.find("div", {"class": "cardImage"})
        self.cardTitle = soup.find("div", {"class": "cardTitle"})
        self.tableRow = self.table.find_all('td')
        self.info = []
        self.header = []

    def getData(self):
        for data in self.tableRow:
            if ":" in data.text or "Type" in data.text:
                self.header.append(data.text.strip())
            elif data.text.strip() is '':
                self.info.append('0')
            else:
                self.info.append(data.text.strip())
        cardInfo = zip(self.header, self.info)
        for infomation in cardInfo:
            print(infomation)

    def createCardCSV(self, csvName):
        """
        Creates CSV from card information scraped
        :param csvName: The name of the CSV file DO NOT INCLUDE .CSV
        :return: Creates CSV file
        """
        with open('{}.csv'.format(csvName), mode='w') as csvFile:
            pokemonWriter = csv.writer(csvFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            pokemonWriter.writerow(self.header)
            pokemonWriter.writerow(self.info)
