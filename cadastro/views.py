from django.shortcuts import render

from cadastro.forms import CadastroUsuarioForm


# Create your views here.
def pagina_cadastro(request):
    formulario = CadastroUsuarioForm()
    if request.method == 'POST':
        formulario = CadastroUsuarioForm(request.POST)
        if formulario.is_valid():
            return render(request, 'login.html')
    return render(request, 'cadastro.html', {'formulario': formulario})
