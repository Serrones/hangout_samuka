from django.db import models

# Create your models here.

class Dono(models.Model):
    nome = models.CharField(max_length=100)
    tel = models.CharField(max_length=13)

    def __str__(self):
        return self.nome

class Animal(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    idade = models.IntegerField()
    dono = models.ForeignKey(Dono, default=1)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    re = models.IntegerField()

    def __str__(self):
        return self.nome

class Atendimento(models.Model):
    animal = models.ForeignKey(Animal, default=1)
    responsavel = models.ForeignKey(Funcionario, default=1)
    consulta = models.DateField(auto_now_add=True)
    observacao = models.TextField(default='')

    def __str__(self):
        return "{} -- {}".format(self.animal, self.consulta)
