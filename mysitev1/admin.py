from django.contrib import admin
from .models import Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin): #'subject' 검색 기능 추가
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)