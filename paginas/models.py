from django.db import models
from datetime import datetime
# Create your models here.
class Apontamento(models.Model):
    nome_usuario = models.CharField(max_length=25, null=True, blank=False)
    hora = models.DateTimeField(default=datetime.now, blank=False)
