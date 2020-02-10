from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Project
from jobs.models import Job


class JobInlineAdmin(admin.StackedInline):
    model = Job
    fields = [
        "order",
        "name",
    ]
    show_change_link = True


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [
        JobInlineAdmin,
    ]


admin.site.register(Project, ProjectAdmin)

# Register your models here.
