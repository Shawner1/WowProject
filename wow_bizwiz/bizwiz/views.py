from django.shortcuts import render, redirect
from django.views import View
from bizwiz.models import *
from bizwiz.forms import *
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 

# Create your views here.

# Home page views it should display industries and tags **Doesn't take in any info from the user**
class HomeView(View):
    def get(self, request):
        industries= Industry.objects.all()
        tag=Tag.objects.all()
        return render(
            request=request, template_name = 'home.html', context = {"industries":industries,"tag":tag}
        )
# Industry views should display industry with its questions and take in a form to add questions
class IndustryView(View):
    def get(self, request, industry_id):
        industry= Industry.objects.get(id=industry_id)
        question= Question.objects.all()
        questions= Question.objects.filter(industry_id=industry_id)
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
                Question.objects.create(question_text=question_description,industry_id=industry_id)
         # "redirect" to the industry page
        return redirect('industry',industry_id=industry_id)

 # Specific_Question views should display industry with its questions and take in a form to add questions   
class Specific_QuestionView(View):
    def get(self,request,industry_id, question_id):
        question= Question.objects.get(id=question_id)
        industry= Industry.objects.get(id=industry_id)
        answer= Answer.objects.all()
        answers= Answer.objects.filter(question_id=question_id)
        form = AnswerForm(initial={'answer_text': Answer.answer_text})
        return render(
            request=request, template_name= 'Specific_Question.html', context={"form":form,"question":question, "industry":industry, "answers":answers,"answer":answer}
        )
    def post(self, request, industry_id,question_id):
        '''Create the answers based on what the user submitted in the form'''
        question = Question.objects.get(id=question_id)
        if 'save' in request.POST:
            form = AnswerForm(request.POST)
            if form.is_valid():
                answer_description = form.cleaned_data['answer']
                Answer.objects.create(answer_text=answer_description,question=question)

        # "redirect" to the specific question page
        return redirect('specific_question',industry_id=industry_id,question_id=question_id)

# Page_for_Tags views should display industries that relate to the tag selected and navigate to page **Doesn't take in any info from the user**
class Page_for_TagsView(View):
    def get(self, request,tag_id):
        tags=Tag.objects.get(id=tag_id)
        industry= Industry.objects.filter(tags=tag_id)
        return render(
             request=request, template_name= 'page_for_tags.html', context={"tags":tags,"industry":industry}
        )
        
# Updating_Page views should taken in a form to update answers to specific questions
class Updating_PageView(View):
    def get(self, request,industry_id,question_id,answer_id):
        answer = Answer.objects.get(id=answer_id)
        industry = Industry.objects.get(id=industry_id)
        question = Question.objects.get(id=question_id)
        form = Updating_PageForm(initial={'update': answer.answer_text})
        return render(
            request=request, template_name = 'Updating_Page.html', context = {"form":form,"answer":answer,"industry":industry,"question":question}
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


#views fot logging in
def homee(request):
    return render(request, "index.html")

def signup(request):

    if request.method =="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']


        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signin')


    return render(request, "signup.html")


def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request, "home.html", {'fname': fname})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('homee')

    return render(request, "signin.html")


def signout(request):
    logout(request)
    messages.success(request, "Logged Out Sucessfully!")
    return redirect('homee')