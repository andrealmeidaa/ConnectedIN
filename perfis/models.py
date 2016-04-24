from django.db import models

class Perfil(models.Model):
    #https://docs.djangoproject.com/en/1.9/ref/models/fields/
    nome=models.CharField(max_length=255,null=False)
    email=models.EmailField(null=False)
    telefone=models.CharField(max_length=20,null=False)
    def convidar(self,perfil_convidado):
        convite=Convite(solicitante=self,convidado=perfil_convidado)
        convite.save()
class Convite(models.Model):
    solicitante=models.ForeignKey(Perfil,related_name='convites_feitos')
    convidado=models.ForeignKey(Perfil, related_name='convites_recebidos')
    
