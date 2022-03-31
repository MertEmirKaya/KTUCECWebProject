from django.contrib import admin
from .models import SurveyModel,QuestionModel,TextAnswerModel,BooleanAnswerModel
# Register your models here.

admin.site.register(SurveyModel)
admin.site.register(QuestionModel)
admin.site.register(TextAnswerModel)
admin.site.register(BooleanAnswerModel)