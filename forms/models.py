from django.db import models
import uuid
# Create your models here.

class Question(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    question=models.CharField(max_length=200,)

    def __str__(self) -> str:
        return self.question

class Survey(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    questions=models.ManyToManyField(Question,)

