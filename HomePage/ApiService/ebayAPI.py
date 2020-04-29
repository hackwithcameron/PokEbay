import json
from decouple import config
import requests


class EbayAPI:

    def __init__(self):
        self.urlProduction = 'https://svcs.ebay.com/services/search/FindingService/v1?'
        self.urlSandBox = 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1'


    def apiRequest(self, keyWords):
        payload = {
            'OPERATION-NAME': 'findCompletedItems',
            'SECURITY-APPNAME': '{0}'.format(config('API_KEY')),  # API_KEY = Production, API_KEY_S = SandBox
            'RESPONSE-DATA-FORMAT': 'JSON',
            'REST-PAYLOAD': '',
            'keywords': keyWords,
            'paginationInput.entriesPerPage': '5',
        }

        data = requests.get(url=self.urlProduction, params=payload)
        response = data.json()
        return response


