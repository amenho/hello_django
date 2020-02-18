from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request,nome):
    return HttpResponse('<h1>Hello {}</h1>'.format(nome))

def soma(request, nro1, nro2):
    total = int(nro1) +  int(nro2)
    return HttpResponse('O resultado da soma de {} e {} é {}'.format(nro1, nro2, total))
