from datetime import date
from django.db import models

class Todo(models.Model):
    nome_aluno = models.CharField(verbose_name="Nome do Aluno",max_length=100, null=False, blank=False) # valores no formato texto
    nome_mae = models.CharField(verbose_name="Nome da Mãe",max_length=100, null=False, blank=False) # valores no formato texto
    cpf_mae = models.CharField(verbose_name="CPF da Mãe",max_length=100, null=False, blank=False) # valores no formato texto
    nome_pai = models.CharField(verbose_name="Nome do Pai",max_length=100, null=False, blank=False) # valores no formato texto
    cpf_pai = models.CharField(verbose_name="CPF do Pai",max_length=100, null=False, blank=False) # valores no formato texto
    endereco = models.CharField(verbose_name="Endereço",max_length=100, null=False, blank=False) # valores no formato texto
    telefone = models.CharField(verbose_name="Telefone",max_length=100, null=False, blank=False) # valores no formato texto
    dt_inicio = models.DateField(null=False, blank=False) 
    mensalidade = models.CharField(verbose_name="Mensalidade",max_length=100, null=False, blank=False) # valores no formato texto
    created_at = models.DateTimeField(auto_now_add=True, null=False, blank=False) #criar o campo que criado automaticamente na data e hora que foi feito o cadastro
    finished_at = models.DateField(null=True) #pode ficar em branco

    class Meta:
        ordering = ["nome_aluno"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
