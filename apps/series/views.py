from django.shortcuts import render, redirect

from serapp.settings import WSDL_URL

from zeep import Client
from cerberus import Validator

client = Client(WSDL_URL)

def validate(request):
    schema = {
        'name': {'type': 'string'},
        'year': {'type': 'integer', 'min': 1900, 'max': 2018},
        'rate': {'type': 'integer', 'min': 0, 'max': 10},
    }
    v = Validator(schema)

    data = {
        "name": request.GET.get('name'),
        "year": int(request.GET.get('year')),
        "rate": int(request.GET.get('rate'))
    }
    return v.validate(data)

def series(request):
    series = client.service.all()
    context = { 'series': series }
    return render(request, 'series/index.html', context)

def create(request):
    context = {}
    return render(request, 'series/create.html', context)

def edit(request, id):
    serie = client.service.findById(id)
    context = { "serie": serie }
    return render(request, 'series/edit.html', context)

def store(request):
    valid = validate(request)

    if (valid):
        data = {
            "name": request.GET.get('name'),
            "year": int(request.GET.get('year')),
            "rate": int(request.GET.get('rate'))
        }
        series = client.service.create(data['name'], data['year'], data['rate'])
        return redirect('/series/list')
    else:
        return redirect('/series/create')

def update(request, id):
    print('update')
    valid = validate(request)
    if (valid):
        data = {
            "name": request.GET.get('name'),
            "year": int(request.GET.get('year')),
            "rate": int(request.GET.get('rate'))
        }
        client.service.update(id, data['name'], data['year'], data['rate'])
        return redirect('/series/list')
    else:
        return redirect(request.META.get('HTTP_REFERER', '/'))

def delete(request, id):
    client.service.delete(id)
    return redirect('/series/list')
