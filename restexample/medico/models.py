# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

ESPECIALIDAD_CHOICES = (
    (u'Angiología', u'Angiología'),
    (u'Cardiología', u'Cardiología'),
    (u'Pediatría', u'Pediatría'),
    (u'Reumatología', u'Reumatología'),
    (u'Urología', u'Urología')
)


class Medico(models.Model):
    identificador = models.IntegerField(verbose_name='id', unique=True)
    nombre = models.CharField(max_length=30)
    apellidos = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    correo = models.EmailField()
    especialidad = models.CharField(max_length=12, choices=ESPECIALIDAD_CHOICES)

    class Meta:
        ordering = ['nombre', 'apellidos']

    def __unicode__(self):
        return '%s %s' % (self.nombre, self.apellidos)