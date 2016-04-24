from django.shortcuts import render,redirect
from perfis.models import Perfil

# Create your views here.

def index(request):
    return render(request,'index.html')
def exibir(request,perfil_id):
    perfil=Perfil.objects.get(id=perfil_id)    
    return render(request,'perfil.html',{"perfil" : perfil})
def listar(request):
    perfis=Perfil.objects.all()
    return render(request,'perfis.html',{"perfis":perfis,
    "perfil_logado":get_perfil_logado(request)})
def convidar(request,perfil_id):
    perfil_convidado=Perfil.objects.get(id=perfil_id)
    perfil_atual=get_perfil_logado(request)
    perfil_atual.convidar(perfil_convidado)
    return redirect('perfil_listar')#Usar o nome da rota
def get_perfil_logado(request):
    return Perfil.objects.get(id=1)
