from django.utils.timezone import datetime
from datetime import timezone
 
from pyexpat import model
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Model created to tag industries and put them into categories
class Tag(models.Model):
    # An ID field is automatically added to all Django models
    #Attribute in tbe model to label the tag name
    tag_name= models.CharField(max_length=50)
class Industry(models.Model):
    # An ID field is automatically added to all Django models
    #Attribute in tbe model to label the industry
    industry_name= models.CharField(max_length=50)
    #Attribute in tbe model to connect many tags to many industries
    tags=models.ManyToManyField(Tag)
class Question(models.Model):
    # An ID field is automatically added to all Django models
    #Attribute in tbe model to have questions in the form of text
    question_text= models.CharField(max_length=255)
    #Attribute in tbe model to connect the question text to a industry
    industry= models.ForeignKey( Industry,on_delete=models.CASCADE)#If industry is deleted all questions are deleted 
    dateposted = models.DateTimeField( auto_now= False, auto_now_add= True )#Time Posted
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #User as foreign key
class Answer(models.Model):
    # An ID field is automatically added to all Django models
    #Attribute in tbe model to connect the answer text to a question
    answer_text= models.CharField(max_length=255)
    #Attribute in tbe model to connect the answer to a question
    question= models.ForeignKey(Question,on_delete=models.CASCADE)#If question is deleted answers are deleted
    dateposted = models.DateTimeField( auto_now= False, auto_now_add= True )#Time Posted
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) #User as foreign key
    likes = models.ManyToManyField(User, related_name='blog_post')

    def total_likes(self):
        return self.likes.count()