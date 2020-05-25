from django.contrib import admin
from . import models

# Register your models here.


class ChoiceInLine(admin.TabularInline):
    model = models.Choice
    extra = 3


@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'publish_date', 'was_published_recently')
    list_filter = ['publish_date']
    search_fields = ['question_text']
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['publish_date'], 'classes': ['collapse']})
    ]
    inlines = [ChoiceInLine]
