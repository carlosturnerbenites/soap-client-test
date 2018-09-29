from django.shortcuts import render
from serapp.settings import WSDL_CALC_URL
from django.views.decorators.csrf import csrf_exempt

from zeep import Client

client = Client(WSDL_CALC_URL)

def calc(request):
    context = {}
    return render(request, 'calc/index.html', context)

@csrf_exempt
def op(request):
    a = request.GET.get('a')
    b = request.GET.get('b')
    op = request.GET.get('op')

    result = None

    if (op == '+'):
      result = client.service.sumar(a, b)
    elif (op == '-'):
      result = client.service.restar(a, b)
    elif (op == '*'):
      result = client.service.multiplicar(a, b)
    elif (op == '/'):
      result = client.service.dividir(a, b)

    context = { "a": a, "b": b, "op": op, "result": result }
    return render(request, 'calc/result.html', context)
