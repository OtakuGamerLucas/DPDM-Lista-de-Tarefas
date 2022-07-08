from django.shortcuts import render, redirect
from .models import Tarefa
from .form import TarefaForm

# Create your views here.

def index(req):
    tarefa = Tarefa.objects.all()

    return render(req, 'index.html', {'tarefa': tarefa})


def cria(req):
    form = TarefaForm(req.POST or None)

    if form.is_valid():
        form.save()
        return redirect('index')
    else:
        return render(req, 'cria.html', {'form': form})


def conclui (req, id):
    tarefa = Tarefa.objects.get(id=id)

    if tarefa.status == 'Ativa':
        tarefa.status = 'Concluída'
        tarefa.btn = 'Ativar'
    else:
        tarefa.status = 'Ativa'
        tarefa.btn = 'Concluir'

    tarefa.save()

    return redirect('index')


def exclui(req, id):
    tarefa = Tarefa.objects.get(id=id)

    if req.method == 'POST':
        tarefa.delete()
        return redirect('index')
    else:
        return render(req, 'confirma_exclui.html', {'tarefa': tarefa})
