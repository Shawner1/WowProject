from django.shortcuts import render,redirect
from .models import * 
from .forms import * 
# Create your views here.

def home(request):
    forums=forum.objects.all()
    count=forums.count()
    conversations=[]
    for i in forums:
        conversations.append(i.conversation_set.all())

    context={'forums':forums,
              'count':count,
              'conversations':conversations}
    return render(request,'home.html',context)

def addInForum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInForum.html',context)

def addInConversation(request):
    form = CreateInConversation()
    if request.method == 'POST':
        form = CreateInConversation(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context ={'form':form}
    return render(request,'addInConversation.html',context)

