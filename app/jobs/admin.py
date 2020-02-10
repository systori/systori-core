from django.contrib import admin
from .models import Job, Chapter, Section, Paragraph, Title, Task, LineItem


class ChapterInline(admin.TabularInline):
    model = Chapter
    show_change_link = True


class SectionInline(admin.TabularInline):
    model = Section
    show_change_link = True


class ParagraphInline(admin.TabularInline):
    model = Paragraph
    show_change_link = True


class TitleInline(admin.TabularInline):
    model = Title
    show_change_link = True


class TaskInline(admin.TabularInline):
    model = Task
    show_change_link = True


class LineItemInline(admin.TabularInline):
    model = LineItem
    show_change_link = True


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    model = Job

    def get_inlines(self, request, obj):
        if obj.tasks.count() == 0:
            return [LineItemInline]
        if obj.titles.count() == 0:
            return [TaskInline]
        if obj.paragraphs.count() == 0:
            return [TitleInline]
        if obj.sections.count() == 0:
            return [ParagraphInline]
        return [ChapterInline]


@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    model = Chapter

    inlines = [
        SectionInline,
    ]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    model = Section

    inlines = [
        ParagraphInline,
    ]


@admin.register(Paragraph)
class ParagraphAdmin(admin.ModelAdmin):
    model = Paragraph

    inlines = [
        TitleInline,
    ]


@admin.register(Title)
class TitleAdmin(admin.ModelAdmin):
    model = Title

    inlines = [
        TaskInline,
    ]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    model = Task

    inlines = [
        LineItemInline,
    ]


@admin.register(LineItem)
class LineItemAdmin(admin.ModelAdmin):
    model = LineItem

