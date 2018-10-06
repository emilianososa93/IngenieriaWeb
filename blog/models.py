from django.db import models
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User

class Post  (models.Model):
    idpublicion = models.ForeignKey(User, on_delete=models.CASCADE)
    idseccion = models.TextField()
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title


class Perfil(models.Model):
    usuario = models.OneToOneField(User,on_delete = models.CASCADE)
    activacion_token= models.CharField(max_length = 40)
    descripcion = models.TextField()


    def __str__(self):
        return self.usuario.username

class Secciones(models.Model):
    idseccion = models.AutoField(primary_key = True)
    descripcion = models.TextField()   
    def __str__(self):
        return self.idseccion   



class Comentario(models.Model):
    idcomentario = models.AutoField(primary_key = True)
    idusuario = models.ForeignKey(User)
    idpublicion = models.ForeignKey(Post)
    texto = models.TextField()
    fechacomentario = models.DateField()
    fechabaja =models.DateField()

    def __str__(self):
        return self.texto

class MotivoDenuncia(models.Model):
    motivo = models.TextField()

    def __str__(self):
        return self.motivo


class Denuncia(models.Model):
    idusuario = models.ForeignKey(User)  
    idcomentario = models.ForeignKey(Comentario)
    fechaDenuncia = models.DateTimeField()
    motivo = models.ForeignKey(MotivoDenuncia)
    idpublicion = models.ForeignKey(Post)

    def __str__(self):
        return str(self.id)


class Perfiles(models.Model):
    idpermiso = models.AutoField(primary_key = True)
    idusuario = models.ForeignKey(User)
    descripcion = models.TextField()

