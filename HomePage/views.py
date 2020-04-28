from django.shortcuts import render
from django.views import View
from .ApiService.ebayAPI import EbayAPI
import json
from Card.views import CardScraper

class IndexView(View):

    def get(self, request):
        # ebayApi = EbayAPI()
        # response = ebayApi.apiRequest('Pokemon Cards')
        # itemPrice = []
    # Pass API response to template
        # context = {
        #     'searchResult': response['findCompletedItemsResponse'][0]['searchResult'][0],
        #     'itemPrice': itemPrice
        # }
        # For dev
        # readable = json.dumps(context, indent=2)
        # Price = response['findCompletedItemsResponse'][0]['searchResult'][0]['item'][0]['sellingStatus'][0]['convertedCurrentPrice'][0].get('__value__')
        # for i in response['findCompletedItemsResponse'][0]['searchResult'][0]:
        #     price = i['item'][0]['sellingStatus'][0]['convertedCurrentPrice'][0].get('__value__')
        #     itemPrice.append(price)
        # print(itemPrice)

        # for i in response['findCompletedItemsResponse'][0]['searchResult'][0]['item']:
        #     for q in i['sellingStatus'][0]['convertedCurrentPrice']:
        #         itemPrice.append(q['__value__'])

        ############## temp ###############
        cardInfo = CardScraper('120')
        cardInfo.getData()

        return render(request, 'HomePage/index.html')
