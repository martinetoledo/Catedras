from django.db import models


class Catedra(models.Model):
    catedra_dias = models.CharField(max_length=250, blank=True)
    catedra_nombre = models.CharField(max_length=250, blank=True)
    catedra_comision = models.CharField(max_length= 250, blank=True)
    catedra_depto = models.CharField(max_length=250, blank=True)
    catedra_materia = models.CharField(max_length=250, blank=True)
    catedra_horario = models.CharField(max_length=250, blank=True)
    catedra_periodo = models.CharField(max_length=250, blank=True)
    catedra_area = models.CharField(max_length=250, blank=True)
    catedra_int = models.CharField(max_length=250, blank=True)
    catedra_puntos = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.catedra_nombre
