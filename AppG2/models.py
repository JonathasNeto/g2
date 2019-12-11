from django.db import models

from django.contrib.auth.models import User


class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    modelo = models.CharField(max_length=15)
    ano = models.CharField(max_length=4)

    def __str__(self):
        return self.modelo

class Departamento(models.Model):
    nome = models.CharField(max_length=15)
    eh_transporte = models.BooleanField(default=False)

    def __str__(self):
        return self.nome

class Cargo(models.Model):
    nome = models.CharField(max_length=15)
    eh_chefe = models.BooleanField(default=False)

    def __str__(self):
        return self.nome
    
class Funcionario(models.Model):
    usuario = models.ForeignKey(User,on_delete=models.CASCADE)
    nome = models.CharField(max_length=150)
    departamento = models.ForeignKey(Departamento,on_delete=models.CASCADE)
    cargo = models.ForeignKey(Cargo,on_delete=models.CASCADE)
    eh_motorista = models.BooleanField(default=False)

    def __str__(self):
        return self.nome+" "+str(self.eh_motorista)


class Solicitacao(models.Model):
    solicitante = models.ForeignKey(Funcionario,on_delete=models.CASCADE)
    origen = models.CharField(max_length=30)
    destino = models.CharField(max_length=30)
    data = models.DateField()
    quantidade = models.IntegerField()
    atendida = models.BooleanField(default=False)
    

    def __str__(self):
        return self.destino


class Atender(models.Model):
    solicitacao = models.ForeignKey(Solicitacao,on_delete=models.CASCADE)
    motorista = models.ForeignKey(Funcionario,on_delete=models.CASCADE,related_name='Motorista')
    veiculo = models.ForeignKey(Veiculo,on_delete=models.CASCADE)

    def __str__(self):
        return self.solicitacao.destino
    




    

    