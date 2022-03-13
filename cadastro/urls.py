from django.urls import path
from cadastro import views


urlpatterns = [
    path('', views.pagina_cadastro, name='cadastro')
]
