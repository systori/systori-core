from django.db import models
from djmoney.models.fields import MoneyField
from projects.models import Project


class Job(models.Model):
    order = models.IntegerField("Reihenfolge")
    name = models.CharField("Bezeichnung", max_length=50)

    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["order"]


class Tasklevel0(models.Model):
    order = models.IntegerField("Reihenfolge")
    name = models.CharField("Bezeichnung", max_length=255)
    unit = models.CharField("Einheit", max_length=3)
    price = MoneyField(max_digits=19, decimal_places=4, default_currency="EUR")

    job = models.ForeignKey(Job, on_delete=models.PROTECT)

    class Meta:
        ordering = ["order"]
