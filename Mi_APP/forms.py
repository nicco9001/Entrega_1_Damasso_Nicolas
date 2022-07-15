from django import forms

class formReclutadores(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    DNI = forms.IntegerField()

class formCandidatos(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    DNI = forms.IntegerField()