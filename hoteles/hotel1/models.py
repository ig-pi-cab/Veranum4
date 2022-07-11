from django.db import models
from django.contrib.auth.models import User #De aqui usaremos un usuario
from django.contrib import admin

# Create your models here.
#Usuario basico. exteiende el usuario de django
class Genero(models.TextChoices):
    HOMBRE = "hombre"
    MUJER = "mujer"
    OTRO= "otro"

class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rut = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    genero = models.CharField(max_length=250, choices=Genero.choices)

    def __str__(self):
        return str(self.user.id) + ' ' + self.user.get_full_name() + ' ' + self.telefono
    
class Habitacion_tipo(models.Model):
    tipo = models.CharField(max_length=50)
    descripcion = models.TextField()
    # picture = models.ImageField(upload_to='habitacion_images', default='habitacion_images/habitacion_no_image.png',null=True)
    rate = models.DecimalField(max_digits=8, decimal_places=2)

    def _str_(self):
        return "{0}: {1}".format(self.pk, self.tipo)


class Habitacion(models.Model):
    room_no         = models.IntegerField(default=101)
    #hotel           = models.ForeignKey(hotel1, on_delete=models.CASCADE)
    tipo_habitacion = models.ForeignKey(Habitacion_tipo, on_delete=models.CASCADE)
    cant_camas      = models.IntegerField()
    precio          = models.IntegerField()
    is_booked       = models.BooleanField(default=False)

    def _str_(self):
        return "{0}: {1}".format(self.pk, self.room_no)

