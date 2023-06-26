from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    
    nombre = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ingrese Nombre"}))
    precio = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Precio"}))
    stock = forms.IntegerField(min_value=0,widget=forms.NumberInput(attrs={"placeholder":"Ingrese Stock"}))
    descripcion = forms.CharField(min_length=10,max_length=200,widget=forms.Textarea(attrs={"rows":4}))

    class Meta:
        model = Producto
        #fields = ['nombre','precio','stock','tipo']
        fields = '__all__'


