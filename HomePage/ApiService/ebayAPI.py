import json
from decouple import config
import requests


class EbayAPI:

    def __init__(self):
        self.urlProduction = 'https://svcs.ebay.com/services/search/FindingService/v1?'
        self.urlSandBox = 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1'
        self.keyWords = ['Pokemon Card', 'Pokemon First Edition', 'Pokemon First Edition',
                    'Pokemon Base', 'Pokemon Jungle', 'Pokemon Fossil',
                    'Pokemon Holo', 'Pokemon Set', 'Pokemon Rare']


    def apiRequest(self):
        payload = {
            'OPERATION-NAME': 'findCompletedItems',
            'SECURITY-APPNAME': '{0}'.format(config('API_KEY')),  # API_KEY = Production, API_KEY_S = SandBox
            'RESPONSE-DATA-FORMAT': 'JSON',
            'REST-PAYLOAD': '',
            'keywords': self.keyWords,
            'paginationInput.entriesPerPage': '20',
        }

        data = requests.get(url=self.urlProduction, params=payload)
        response = data.json()
        readable = json.dumps(response['findCompletedItemsResponse'][0]['searchResult'][0], indent=2)
        items = json.loads(readable.replace('__', '').replace('@', ''))
        return items

    def apiUpdate(self):
        pass



