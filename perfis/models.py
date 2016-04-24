from django.db import models

class Perfil(models.Model):
    #https://docs.djangoproject.com/en/1.9/ref/models/fields/
    nome=models.CharField(max_length=255,null=False)
    email=models.EmailField(null=False)
    telefone=models.CharField(max_length=20,null=False)
    
