from django import forms

class Updating_PageForm(forms.Form):
    answer = forms.CharField(label='Update Answer Here', max_length=255)