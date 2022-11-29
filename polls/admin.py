from .models import Question, Choice
from django.contrib import admin
from .models import Profile

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]


admin.site.register(Profile)

admin.site.register(Question, QuestionAdmin)
