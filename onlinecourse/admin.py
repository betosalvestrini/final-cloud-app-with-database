from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

class QuestionInline(admin.StackedInline):
    model = Question
    extra = 5

class LessonInline(admin.StackedInline):
    model = Lesson
    extra = 5
    inlines = [QuestionInline]  # Встроенные вопросы

class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]
    list_display = ['title']

class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'description']

admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
