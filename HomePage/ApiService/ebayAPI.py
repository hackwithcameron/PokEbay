import json

from decouple import config
import requests


class EbayAPI:

    def __init__(self):
        self.urlProduction = 'https://svcs.ebay.com/services/search/FindingService/v1?'
        self.urlSandBox = 'https://svcs.sandbox.ebay.com/services/search/FindingService/v1'

    def apiRequest(self):
        payload = {
            'OPERATION-NAME': 'findCompletedItems',
            'SECURITY-APPNAME': '{0}'.format(config('API_KEY_S')),
            'RESPONSE-DATA-FORMAT': 'JSON',
            'REST-PAYLOAD': '',
            'keywords': 'Card',
        }

        data = requests.get(url=self.urlSandBox, params=payload)
        response = data.json()
        # response = json.loads(data.text)
        return response


