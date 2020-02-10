from django.contrib import admin
from .models import Job, Tasklevel0


class Tasklevel0Inline(admin.TabularInline):
    model = Tasklevel0


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job

    inlines = [
        Tasklevel0Inline,
    ]


@admin.register(Tasklevel0)
class Tasklevel0Admin(admin.ModelAdmin):
    model = Tasklevel0

