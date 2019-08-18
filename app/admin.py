from django.contrib import admin
from .models import SimulaModel,CarroLojaModel,LojaModel,CarroApi

admin.site.register(SimulaModel)
admin.site.register(CarroLojaModel)
admin.site.register(LojaModel)
admin.site.register(CarroApi)

# Register your models here.
