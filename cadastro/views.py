from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def pagina_cadastro(request):
    return HttpResponse('<html><title>Cadastro</title></html>')
