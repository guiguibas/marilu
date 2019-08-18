from django.urls import path
from .views import SimulaView, simula_api,carro_loja_api, loja_api, carro_api
from django.conf.urls import url

urlpatterns = [
    path('SimuladorFinanciamento', SimulaView,),
    url(r'^simula', simula_api.as_view(), name='simula'),
    url(r'^carro_loja_api', carro_loja_api.as_view(), name='carro_loja_api'),
    url(r'^loja_api', loja_api.as_view(), name='loja_api'),
    url(r'^carro_api', carro_api.as_view(), name='carro_api')
]