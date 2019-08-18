from django.forms import  ModelForm
from .views import SimulaModel


class SimulaForm(ModelForm):
    class Meta:
        model = SimulaModel
        fields = '__all__'