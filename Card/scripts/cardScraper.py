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
        """
        Filters BS results
        :return: Card information as dictionary
        """
        for data in self.tableRow:
            if "species" in data.text.lower() or "cards" in data.text.lower():
                continue
            if ":" in data.text or "type" in data.text.lower():
                self.header.append(data.text.strip(":"))
            elif data.text.strip() is '':
                self.info.append('0')
            else:
                self.info.append(data.text.strip())
        # Coverts list into dictionary
        cardDict = {self.header[i]: self.info[i] for i in range(len(self.header))}
        # Creates dictionary of card name and img
        titleDict = {
            'Name': self.cardTitle.text.strip()[3:],
            'imgLink': self.cardImg.img['src']
        }
        # Cleans dictionary keys by removing spaces
        cardDictClean = {k.replace(' ', ''): v for k, v in cardDict.items()}
        cardDictClean.update(titleDict)
        return cardDictClean


    def createCardCSV(self, csvName):
        """
        Creates CSV from card information scraped
        :param csvName: The name of the CSV file DO NOT INCLUDE .CSV
        :return: Creates CSV file
        """
        cardDict = {self.header[i]: self.info[i] for i in range(len(self.header))}
        with open('{}.csv'.format(csvName), mode='w') as csvFile:
            fieldnames = self.header
            pokemonWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            pokemonWriter.writeheader()
            pokemonWriter.writerow(cardDict)
