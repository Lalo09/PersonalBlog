from django.db import models

class EntryManager(models.Manager):
    """Procedimiento para entrada de portada"""

    def entrada_en_portada(self):
        #Devuelve la entrada de portada
        return self.filter(
            public  = True,
            portada = True,
        ).order_by('-created').first()

    def entradas_en__home(self):
        #Devuelve ultimas 4 entradas
        return self.filter(
            public  = True,
            in_home = True,
        ).order_by('-created')[:4]

    def entradas_recientes(self):
        #Devuelvelas ultimas 6 entradas recientes
        return self.filter(
            public  = True
        ).order_by('-created')[:6]

    def buscar_entrada(self,kword,categoria):
        #Buscar entradas por categoria o palabra clave
        if len(categoria) > 0:
            return self.filter(
                category__short_name=categoria,
                title__icontains=kword,
                public=True
            ).order_by('-created')
        else:
            return self.filter(
                title__icontains=kword,
                public=True
            ).order_by('-created')
