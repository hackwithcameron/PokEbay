from django.shortcuts import render
from django.views import View
from .ApiService.ebayAPI import EbayAPI
import json


class Index(View):

    def get(self, request):
        ebayApi = EbayAPI()
        items = ebayApi.apiRequest()

        # Pass API response to template
        context = {
            'items': items,
        }

        return render(request, 'HomePage/index.html', context)
