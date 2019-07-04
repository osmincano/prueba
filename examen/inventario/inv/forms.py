from django import forms
from .models import *

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ('serie', 'cantidad', 'precio')
