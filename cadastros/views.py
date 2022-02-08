from dataclasses import fields
from re import template
from xml.parsers.expat import model
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView

# Create your views here.

# serve para redirecionar a pagina
from django.urls import reverse_lazy

from cadastros.models import Clientes

# Paginá Criar - C
class ClientesCad(CreateView):
    model = Clientes
    fields = ['nome', 'email']
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

# Pagina Listar - R
class ClientesListagem(ListView):
    model = Clientes
    template_name = 'cadastros/listar_cadastros.html'

# Pagina update - U
class ClientesUpdate(UpdateView):
    model = Clientes
    fields = "__all__"
    template_name = 'cadastros/index_cadastros.html'
    success_url = reverse_lazy('listagem')

# Pagina deletar - D
class ClientesDelete(DeleteView):
    model = Clientes
    fields = "__all__"
    template_name = 'cadastros/excluir_cadastros.html'
    success_url = reverse_lazy('listagem')

def abertura_modelform(request):
    return render(request, "index.html")
