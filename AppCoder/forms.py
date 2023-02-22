from django import forms

class MedicinaFormulario(forms.Form):
    nombre = forms.CharField()
    presentacion = forms.CharField()
    caducidad = forms.DateField()
    existencia = forms.BooleanField()

class ComestibleFormulario(forms.Form):
    nombre = forms.CharField()
    tamano = forms.IntegerField()
    caducidad = forms.DateField()
    existencia = forms.BooleanField()

class LimpiezaFormulario(forms.Form):
    nombre = forms.CharField()
    presentacion = forms.CharField()
    tamano = forms.IntegerField()
    existencia = forms.BooleanField()