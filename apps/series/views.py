from django.shortcuts import render
from serapp.settings import WSDL_URL

from zeep import Client

client = Client(WSDL_URL)

def series(request):
    print('series')
    series = client.service.all()
    print(series)
    context = { 'series': series }
    return render(request, 'series/index.html', context)

def create(request):
    print('create')
    context = {}
    return render(request, 'series/create.html', context)

def edit(request):
    print('edit')
    context = {}
    return render(request, 'series/edit.html', context)

def store(request):
    print('store')
    context = {}
    print(request.GET)
    series = client.service.create(
        request.GET.get('name'),
        request.GET.get('year'),
        request.GET.get('rate')
    )
    # return render(request, 'series/index.html', context)
    return series(request) # redirect('/series')


def update(request):
    print('update')
    context = {}
    return render(request, 'series/index.html', context)

def delete(request):
    print('delete')
    context = {}
    return render(request, 'series/index.html', context)
