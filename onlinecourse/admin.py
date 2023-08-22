from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3  # Number of choices to display for each question

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1  # Number of questions to display for each course

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class CourseAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Course, CourseAdmin)
