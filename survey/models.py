from django.db import models
import uuid
# Create your models here.




class QuestionModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False) 
    
    text=models.CharField(max_length=255,)


    def __str__(self) -> str:
        return self.text



class SurveyModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)    
    title=models.CharField(max_length=155)
    pub_date=models.DateTimeField(auto_now_add=True,verbose_name='published date')
    questions=models.ManyToManyField(QuestionModel,null=True,blank=True)

    def __str__(self) -> str:
        return self.title


class TextAnswerModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False) 
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    
    textAnswer=models.TextField()
    
    def __str__(self) -> str:
        return self.textAnswer

class BooleanAnswerModel(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)     
    question=models.ForeignKey(QuestionModel,on_delete=models.CASCADE)
    answer=models.BooleanField()

    def __str__(self) -> str:
        return str(self.answer)