from django.forms import ModelForm
from .models import *

class CreateInForum(ModelForm):
    class Meta:
        model= forum
        fields = "__all__"

class CreateConversation(ModelForm):
    class Meta:
        model= Conversation
        fields = "__all__"