from django import forms
from .models import Registrado, Contacto

class RegModelForm(forms.ModelForm):
    class Meta:
        model = Registrado
        fields = ["nombre", "email"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "edu":
            raise forms.ValidationError("Por favor utiliza un email con la extension .EDU")
        return email

    def clean_nombre(self):
        nombre = self.cleaned_data.get("nombre")
        #validaciones
        return nombre

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ["nombre", "email", "mensaje"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        email_base, proveedor = email.split("@")
        dominio, extension = proveedor.split(".")
        if not extension == "com":
            raise forms.ValidationError("Por favor utiliza un email con la extension .EDU")
        return email
