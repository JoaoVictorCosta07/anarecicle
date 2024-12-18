from django.db import models

class Material(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Dia(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Coleta(models.Model):
    # Campos para endereço
    rua = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    bairro = models.CharField(max_length=100)

    # Campo para materiais recicláveis
    materiais = models.ManyToManyField(Material)

    # Campo para dias de coleta
    dias = models.ManyToManyField(Dia)

    # Campo para turno de coleta
    TURNO_CHOICES = [
        ('manha', 'Manhã'),
        ('tarde', 'Tarde'),
        ('noite', 'Noite'),
    ]
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES, blank=False)

    def __str__(self):
        return f'Coleta em {self.rua}, {self.numero} - {self.bairro}'
