from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Updating_PageForm(forms.Form):
    update = forms.CharField(label='Update Answer Here', max_length=255)
class QuestionForm(forms.Form):
    question = forms.CharField(label='Enter Question', max_length=255)
class AnswerForm(forms.Form):
    answer = forms.CharField(label='Answer Here', max_length=255)
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']