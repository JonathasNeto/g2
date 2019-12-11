from django.urls import path
from . import views

urlpatterns = [
    path('',views.inicio,name='Inicio'),
    path('solicitar/',views.solicitar,name='Solicitar'),
    path('atender/',views.atender,name='atender'),
    path('atender/atendimentos/',views.atendimentos,name='Atendimentos'),
    path('atender/atendimentos/<int:id>/',views.detalhesat,name='Detalhes'),
    
]