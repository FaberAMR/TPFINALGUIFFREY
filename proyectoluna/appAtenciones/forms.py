from django import forms

class CargarMascota(forms.Form):
    name=forms.CharField()
    peso=forms.FloatField()
    