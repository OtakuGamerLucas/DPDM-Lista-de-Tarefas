from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cria', views.cria, name='cria'),
    path('conclui/<int:id>', views.conclui, name='conclui'),
    path('exclui/<int:id>', views.exclui, name='exclui')
    
]