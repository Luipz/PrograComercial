from django.db import models

# Create your models here.
from django.utils import timezone

class Publicacion(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    fecha_creacion = models.DateTimeField(verbose_name='Creado',
            default=timezone.now)
    fecha_publicacion = models.DateTimeField(
    blank=True, null=True)

    def publicar(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def _str_(self):
        return self.titulo 

    class Meta:
        verbose_name_plural = 'Publicaciones'
