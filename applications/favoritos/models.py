from enum import unique
from django.db import models
from django.conf import settings
from applications.users.models import User

from model_utils.models import TimeStampedModel
from applications.entrada.models import Entry
from .managers import FavoritesManager

class Favorites(TimeStampedModel):
    """Modelo para favoritos"""

    user = models.ForeignKey(
        User,
        related_name='user_favorites',
        on_delete=models.CASCADE
    )
    entry = models.ForeignKey(
        Entry,
        related_name='entry_favorites',
        on_delete=models.CASCADE
    )

    objects = FavoritesManager()

    class Meta:
        unique_together = ('user','entry') #Que no sean iguales
        verbose_name = 'Entrada Favorita'
        verbose_name_plural = "Entradas Favoritas"

    def __str__(self):
        return self.entry.title