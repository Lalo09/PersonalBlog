from datetime import timedelta,datetime

from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse_lazy
from applications.users.models import User 

from model_utils.models import TimeStampedModel
from ckeditor_uploader.fields import RichTextUploadingField

#Managers
from .managers import EntryManager

class Category(TimeStampedModel):
    """Categorias para una entrada"""

    short_name = models.CharField(
        'Nombre corto',
        max_length=15,
        unique=True
    )
    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    def __str__(self):
        return self.name

class Tag(TimeStampedModel):
    """Etiquetas para un articulo"""

    name = models.CharField(
        'Nombre',
        max_length=30
    )

    class Meta:
        verbose_name = 'Etiqueta'
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name

class Entry(TimeStampedModel):
    """Una entrada de blog"""

    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    title = models.CharField(
        'Titulo',
        max_length=200
    )
    resume = models.TextField('Resumen')
    content = RichTextUploadingField('Contenido')
    public = models.BooleanField(default=False)
    image = models.ImageField(
        'Imagen',
        upload_to = 'Entry'
    )
    portada = models.BooleanField(default=False)
    in_home = models.BooleanField(default=False)
    slug = models.SlugField(editable=False,max_length=300)

    objects = EntryManager()

    class Meta:
        verbose_name = 'Entrada'
        verbose_name_plural = 'Entradas'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy(
            'entrada_app:entradadetalle',
            kwargs={
                'slug':self.slug
            }
        )

    def save(self, *args, **kwargs):
        #Calculamos el total de segundos de la hora actual
        now = datetime.now()
        total_time = timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
        seconds = int(total_time.total_seconds())
        slug_unique =  '%s %s' % (self.title,str(seconds))

        self.slug = slugify(slug_unique)

        super(Entry,self).save(*args,**kwargs)