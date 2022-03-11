from django.shortcuts import render


# Create your views here.
def pagina_cadastro(request):
    if request.method == 'POST':
        return render(request, 'login.html')
    return render(request, 'cadastro.html')

