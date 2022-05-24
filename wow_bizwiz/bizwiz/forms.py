from django import forms

class Updating_PageForm(forms.Form):
    update = forms.CharField(label='Update Answer Here', max_length=255)
class QuestionForm(forms.Form):
    question = forms.CharField(label='Enter Question', max_length=255)
class AnswerForm(forms.Form):
    answer = forms.CharField(label='Answer Here', max_length=255)