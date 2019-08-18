from django.urls import path
from .views import SimulaView, simula
from django.conf.urls import url

urlpatterns = [
    path('SimuladorFinanciamento', SimulaView,),
    url(r'^simula', simula.as_view(), name='simula')

]