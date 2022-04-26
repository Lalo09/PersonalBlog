from django.db import models
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    """Modelo de pagina principal"""

    title = models.CharField(
        'Nombre',
        max_length=30
    )
    description = models.TextField()
    about_title = models.CharField(
        'Titulo Nosotros',
        max_length=50
    )
    about_text = models.TextField()
    contact_email = models.EmailField(
        'email de contacto',
        blank=True,
        null=True
    )
    phone = models.CharField(
        'Telefono de contacto',
        max_length=20
    )

    class Meta:
        verbose_name = 'Pagina Principal'
        verbose_name_plural = 'Pagina Principal'

    def __str__(self):
        return self.title

class Subscribers(TimeStampedModel):
    """Modelo de subscriptores"""

    email = models.EmailField()

    class Meta:
        verbose_name = 'Subscriptor'
        verbose_name_plural = 'Subscriptores'

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):
    """Modelo de mensajes de formulario de contacto"""

    full_name = models.CharField(
        "Nombres", 
        max_length=50
    )
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Mensajes'

    def __str__(self):
        return self.full_name
            