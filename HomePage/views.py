from django.shortcuts import render
from django.views import View
from .ApiService.ebayAPI import EbayAPI
import json



class IndexView(View):

    def get(self, request):
        response = EbayAPI.apiRequest(EbayAPI())
        context = {
            'searchResult': response['findCompletedItemsResponse'][0]['searchResult'][0],
        }
        readable = json.dumps(context, indent=2)
        print(readable)

        return render(request, 'HomePage/index.html', context)
