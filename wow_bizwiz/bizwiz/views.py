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
        industry= Industry.objects.get(pk=industry_id)
        return render(
            request=request, template_name= 'Industry.html', context={'industry':industry}
        )

 # Specific_Question views should display industry with its questions and take in a form to add questions   
class Specific_QuestionView(View):
    def get(self,request,industry_id, question_id,answer_id):
        question= Question.objects.get(id=question_id)
        industry= Industry.objects.get(id=industry_id)
        answer= Industry.objects.get(id=answer_id)
        return render(
            request=request, template_name= 'Specific_Question.html', context={"question":question, "industry":industry, "answer":answer}
        )

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
                answers = form.cleaned_data['answer']
                answer.update(answer_text=answers)
        elif 'delete' in request.POST:
            answer.delete()
        # "redirect" to the specific question page
        return redirect('specific_question')
