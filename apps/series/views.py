from django.shortcuts import render
from serapp.settings import WSDL_URL

from zeep import Client

client = Client(WSDL_URL)

def index(request):
    hello = client.service.hello('World')
    series = []
    series = client.service.all()
    print(series)
    context = { 'hello' : hello, 'series': series }
    return render(request, 'series/index.html', context)
