from django.urls import path
from .views import SimulaView, simula_api
from django.conf.urls import url

urlpatterns = [
    path('SimuladorFinanciamento', SimulaView,),
    url(r'^simula', simula_api.as_view(), name='simula')

]