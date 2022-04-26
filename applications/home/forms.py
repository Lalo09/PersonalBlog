from django import forms
from .models import Contact, Subscribers

class SuscriberForm(forms.ModelForm):
    """Formulario para el registro de subscribirse"""

    class Meta:
        model = Subscribers
        fields = (
            'email',
        )
        widgets = {
            'email':forms.EmailInput(
                attrs={
                    'placeholder':"Ingresa tu correo...",
                }
            ),
        }

class ContactForm(forms.ModelForm):
    """Formulario de contacto"""
    class Meta:
        model = Contact
        fields = ('__all__')
