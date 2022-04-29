from pyexpat import model
from django.db import models

# Create your models here.


class Tag(models.Model):
    # An ID field is automatically added to all Django models
    tag_name= models.CharField(max_length=50)

class Industry(models.Model):
    # An ID field is automatically added to all Django models
    industry_name= models.CharField(max_length=50)
    tags=models.ManyToManyField(Tag)
class Question(models.Model):
    # An ID field is automatically added to all Django models
    question_text= models.CharField(max_length=255)
    industry= models.ForeignKey( Industry,on_delete=models.CASCADE)#If industry is deleted all questions are deleted 
class Answer(models.Model):
    # An ID field is automatically added to all Django models
    answer_text= models.CharField(max_length=255)
    question= models.ForeignKey(Question,on_delete=models.CASCADE)#If question is deleted answers are deleted