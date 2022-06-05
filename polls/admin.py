from django.contrib import admin
from .models import Question, Choice, TaggedItem
# Register your models here.

class TaggedItemAdmin(admin.ModelAdmin):
    fields = ('tag', 'content_type', 'object_id', 'content_object')
    readonly_fields = ['content_object']
    
    class Meta:
        model = TaggedItem

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None,               {'fields': ['question_text']}),
    #     ('Date information', {'fields': ['pub_date']}),
    # ]
    list_display = ('question_text', 'pub_date')
    # inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(TaggedItem, TaggedItemAdmin)
