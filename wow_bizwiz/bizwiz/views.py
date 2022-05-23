from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from bizwiz.models import *
from bizwiz.forms import *

# Create your views here.

# Home page views it should display industries and tags **Doesn't take in any info from the user**
class HomeView(View):
    def get(self, request):
        industries= Industry.objects.all()
        return render(
            request=request, template_name = 'home.html', context = {"industries":industries}
        )
# Industry views should display industry with its questions and take in a form to add questions
class IndustryView(View):
    def get(self, request, industry_id):
        industry= Industry.objects.get(id=industry_id)
        question= Question.objects.all()
        form = QuestionForm(initial={'question_text': Question.question_text})
        return render(
            request=request, template_name= 'Industry.html', context={'industry':industry,'form':form,'question':question}
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
        answers= Answer.objects.all()
        form = AnswerForm(initial={'answer_text': Answer.answer_text})
        return render(
            request=request, template_name= 'Specific_Question.html', context={"form":form,"question":question, "industry":industry, "answers":answers}
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

# Page_for_Tags views should display industries that relate to the tag selected **Doesn't take in any info from the user**
class Page_for_TagsView(View):
    def get(self, request,tag_id):

        return render(
            request=request, template_name = 'Page_for_Tags.html', context = {}
        )
# Updating_Page views should taken in a form to update answers to specific questions
class Updating_PageView(View):
    def get(self, request,industry_id,question_id,answer_id):
        answer = Answer.objects.get(id=answer_id)
        industry = Industry.objects.get(id=industry_id)
        question = Question.objects.get(id=question_id)
        form = Updating_PageForm(initial={'answer_text': Answer.answer_text})
        return render(
            request=request, template_name = 'Updating_Page.html', context = {"form":form,"answer":answer,"industry":industry,"question":question}
        )
    def post(self, request, answer_id,industry_id,question_id):
        '''Update or delete the specific answers based on what the user submitted in the form'''
        answer = Answer.objects.filter(id=answer_id)
        industry = Industry.objects.get(id=industry_id)
        question = Question.objects.get(id=question_id)
        if 'save' in request.POST:
            form = Updating_PageForm(request.POST)
            if form.is_valid():
                answers = form.cleaned_data['update']
                answer.update(answer_text=answers)
        elif 'delete' in request.POST:
            answer.delete()
        # "redirect" to the specific question page
        return redirect('specific_question',industry_id=industry_id,question_id=question_id)
