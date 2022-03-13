from django.urls import path
from login import views


urlpatterns = [
    path('', views.pagina_login, name='login')
]
