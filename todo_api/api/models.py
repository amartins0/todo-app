# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from taggit.managers import TaggableManager


# Create your models here.

class Tarefa(models.Model):
    titulo = models.CharField(max_length=200)
    completa = models.BooleanField(default=False)
    descricao = models.CharField(max_length=200)

    objects = models.Manager()
    tags = TaggableManager()

    def __str_(self):
        return self.titulo
