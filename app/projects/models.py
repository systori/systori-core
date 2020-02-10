from django.db import models
from django.contrib.postgres.fields import ArrayField


# class Paragraph(models.Model):
#     text = models.TextField("text")

#     def __str__(self):
#         return f"<Paragraph: {self.text[:30]}>"


# class BulletpointList(models.Model):
#     points = ArrayField(models.CharField(max_length=30, blank=True))

#     def __str__(self):
#         return f"<BulletpointList: {[point[:10] for point in self.points]}>"


class Project(models.Model):
    name = models.CharField("Name", help_text="Ein schöner Projektname.", max_length=30)
    date = models.DateField("Datum")
    # paragraphs = models.ManyToManyField(Paragraph, related_name="paragraphs")
    # bulletpoint_lists = models.ManyToManyField(
    #     BulletpointList, related_name="bulletpoint_lists"
    # )

    def __str__(self):
        return f"{self.name} ({self.date:%B %Y})"
