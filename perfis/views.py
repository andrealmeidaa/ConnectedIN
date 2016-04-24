from django.shortcuts import render
from perfis.models import Perfil

# Create your views here.

def index(request):
    return render(request,'index.html')
def exibir(request,perfil_id):
    perfil=Perfil()
    if (perfil_id=='1'):
        perfil=Perfil('André Almeida','andre@mail.com','9899-8956')
        
    return render(request,'perfil.html',{"perfil" : perfil})
