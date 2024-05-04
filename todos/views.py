from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from datetime import date
from .models import Todo

class TodoListView(ListView):
    model = Todo

class TodoCreateView(CreateView):
    model = Todo
    fields = ["nome_aluno", "nome_mae", "cpf_mae", "nome_pai", "cpf_pai", "endereco", "telefone", "dt_inicio", "mensalidade"]
    success_url = reverse_lazy ("todo_list")

class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["nome_aluno", "nome_mae", "cpf_mae", "nome_pai", "cpf_pai", "endereco", "telefone", "dt_inicio", "mensalidade"]
    success_url = reverse_lazy ("todo_list")

class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
