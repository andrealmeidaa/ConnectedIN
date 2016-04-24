from django.conf.urls import url
"""
Importa o módulo views da app perfis
Passa como referência o método que irá apresentar
a resposta a requisição

Expressoes Regulares
^ --> Determinar que a string deve aparecer no começo
$ --> Finaliza a string
Como aqui já entrou pelo perfis, daqui em diante é obrigado entrar
a expressão perfis no browser
Para poder pegar o parâmetro, precisamos criar um grupo
dentro da expressão regular para fazer a separação

O 3 parâmetro nomei a rota, o que evita problemas se a rota propriamente dita
for renomeada
"""
from perfis.views import *
urlpatterns = [
    url(r'^$',index),
    url(r'^exibir/(?P<perfil_id>\d+)$',exibir,name='perfil_exibir'),
    url(r'^listar$',listar,name='perfil_listar'),
    url(r'^exibir/(?P<perfil_id>\d+)/convidar$',convidar,name='perfil_convidar')
    
]