from multiprocessing import context
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from bizwiz.models import *
from bizwiz.forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse 

def LikeView(request,industry_id,question_id,answer_id):
    post = get_object_or_404(Answer, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    answer = Answer.objects.get(id=answer_id)
    industry = Industry.objects.get(id=industry_id)
    question = Question.objects.get(id=question_id)
    return redirect('updating_page', industry_id=industry_id,question_id=question_id, answer_id = answer_id)


# Create your views here.
#views for signing up 
def registerPage(request):
    form = CreateUserForm()
    if request.user.is_authenticated:
        return redirect('home')
    else:
         if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "Your Account has been successfully created for "+  user)
                return redirect('signin')
    context = {'form':form}
    return render(request, "register.html",context)
#views for signing in 
def signin(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST['username']
            pass1 = request.POST['pass1']

            user = authenticate(username=username, password=pass1)

            if user is not None:
                login(request, user)
                user = username
                messages.success(request, "Your Account has been successfully signed in "+  user)
                return redirect('home')


            else:
                messages.error(request, "Username Or Password is incorrect")
                return redirect("signin")

        return render(request, "signin.html")

#views for signing out
def signout(request):
        logout(request)
        messages.success(request, "Your Account has been successfully signed out ")
        return redirect("signin")

# Home page views it should display industries and tags **Doesn't take in any info from the user**

@method_decorator(login_required(login_url='signin'), name='dispatch')
class HomeView(View):
    def get(self, request):
        industries= Industry.objects.all()
        tag=Tag.objects.all()
        return render(
            request=request, template_name = 'home.html', context = {"industries":industries,"tag":tag}
        )
# Industry views should display industry with its questions and take in a form to add questions
@method_decorator(login_required(login_url='signin'), name='dispatch')
class IndustryView(View):
    def get(self, request, industry_id):
        industry= Industry.objects.get(id = industry_id)
        question= Question.objects.all()
        questions= Question.objects.filter(industry_id = industry_id)
        form = QuestionForm(initial={'question_text': Question.question_text})
        return render(
            request=request, template_name= 'Industry.html', context={'industry':industry,'form':form,'question':question,'questions':questions}
        )
    def post(self, request, industry_id):
        '''post questions based on what the user submitted in the form'''
        if 'save' in request.POST:
            form = QuestionForm(request.POST)
            if form.is_valid():
                question_description = form.cleaned_data['question']
                instance = request.user
                Question.objects.create(question_text=question_description,industry_id=industry_id, user = instance)
                
         # "redirect" to the industry page
        return redirect('industry',industry_id=industry_id)

 # Specific_Question views should display industry with its questions and take in a form to add questions  
@method_decorator(login_required(login_url='signin'), name='dispatch') 
class Specific_QuestionView(View):
    def get(self,request,industry_id, question_id):
        question= Question.objects.get(id=question_id)
        industry= Industry.objects.get(id=industry_id)
        answer= Answer.objects.all()
        answers= Answer.objects.filter(question_id=question_id)
        form = AnswerForm(initial={'answer_text': Answer.answer_text})
        return render(
            request=request, template_name= 'Specific_Question.html', context={"form":form, "question":question, "industry":industry, "answers":answers,"answer":answer}
        )
    def post(self, request, industry_id, question_id):
        '''Create the answers based on what the user submitted in the form'''
        question = Question.objects.get(id=question_id)
        if 'save' in request.POST:
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer_description = form.cleaned_data['answer']
                instance = request.user
                Answer.objects.create(answer_text=answer_description,question=question,user= instance)

        # "redirect" to the specific question page
        return redirect('specific_question',industry_id=industry_id,question_id=question_id)

# Page_for_Tags views should display industries that relate to the tag selected and navigate to page **Doesn't take in any info from the user**
@method_decorator(login_required(login_url='signin'), name='dispatch')
class Page_for_TagsView(View):
    def get(self, request,tag_id):
        tags=Tag.objects.get(id=tag_id)
        industry= Industry.objects.filter(tags=tag_id)
        return render(
             request=request, template_name= 'page_for_tags.html', context={"tags":tags,"industry":industry}
        )
        
# Updating_Page views should taken in a form to update answers to specific questions
@method_decorator(login_required(login_url='signin'), name='dispatch')
class Updating_PageView(View):
    def get(self, request,industry_id,question_id,answer_id):
        answer = Answer.objects.get(id=answer_id)
        industry = Industry.objects.get(id=industry_id)
        question = Question.objects.get(id=question_id)
        form = Updating_PageForm(initial={'update': answer.answer_text})
        post = get_object_or_404(Answer, id=answer_id)
        total_likes=post.total_likes()
        return render(
            request=request, template_name = 'Updating_Page.html', context = {"form":form,"answer":answer,"industry":industry,"question":question,"total_likes":total_likes}
        )
    def post(self, request, answer_id,industry_id,question_id):
        '''Update or delete the specific answers based on what the user submitted in the form'''
        answer = Answer.objects.filter(id=answer_id)
        if 'save' in request.POST:
            form = Updating_PageForm(request.POST)
            if form.is_valid():
                answers = form.cleaned_data['update']
                answer.update(answer_text=answers)
        elif 'delete' in request.POST:
            answer.delete()
        # "redirect" to the specific question page
        return redirect('specific_question',industry_id=industry_id,question_id=question_id)
