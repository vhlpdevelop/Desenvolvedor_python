from django.db import models

#Model de exemplo usuario

class User(models.Model):
    nome = models.CharField('nome',max_length=30)
    telefone = models.BigIntegerField('telefone')
    email = models.CharField('Email', max_length=30)

    def __str__(self):
        return f"Nome:{self.nome}, Telefone:{self.telefone}, Email:{self.email}"

