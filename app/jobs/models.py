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


class Chapter(models.Model):
    order = models.IntegerField("Reihenfolge")
    name = models.CharField("Bezeichnung", max_length=50)

    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="chapters")

    class Meta:
        ordering = ["order"]


class Section(models.Model):
    order = models.IntegerField("Reihenfolge")
    name = models.CharField("Bezeichnung", max_length=50)

    group = models.ForeignKey(Chapter, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="sections")

    class Meta:
        ordering = ["order"]


class Paragraph(models.Model):
    order = models.IntegerField("Reihenfolge")
    name = models.CharField("Bezeichnung", max_length=50)

    group = models.ForeignKey(Section, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="paragraphs")

    class Meta:
        ordering = ["order"]


class Title(models.Model):
    order = models.IntegerField("Reihenfolge")
    name = models.CharField("Bezeichnung", max_length=50)

    group = models.ForeignKey(Paragraph, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="titles")

    class Meta:
        ordering = ["order"]


class Task(models.Model):
    order = models.IntegerField("Reihenfolge")
    index = models.IntegerField("Index")
    name = models.CharField("Bezeichnung", max_length=255)
    description = models.TextField("Beschreibung")
    unit = models.CharField("Einheit", max_length=10)

    group = models.ForeignKey(Title, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="tasks")

    class Meta:
        ordering = ["order"]


class LineItem(models.Model):
    order = models.IntegerField("Reihenfolge")
    name = models.CharField("Bezeichnung", max_length=255)
    unit = models.CharField("Einheit", max_length=10)
    price = MoneyField(max_digits=17, decimal_places=2, default_currency="EUR")

    task = models.ForeignKey(Task, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT, related_name="lineitems")

    class Meta:
        ordering = ["order"]
