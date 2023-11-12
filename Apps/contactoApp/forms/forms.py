""" Formulario de Contacto """

from django import forms


class ContactoForm(forms.Form):
    """ Clase de Formulario para Contacto """
    nombre = forms.CharField(label="Nombre",  required=True, max_length=50)
    email = forms.CharField(label="Email",  required=True, max_length=30)
    contenido = forms.CharField(label="Contenido", widget=forms.Textarea)
