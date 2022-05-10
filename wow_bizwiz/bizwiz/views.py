from django.shortcuts import render
from django.views import View
from bizwiz.models import *

# Create your views here.

# Home page views it should display industries and tags **Doesn't take in any info from the user**
class HomeView(View):
    def get(self, request):

        return render(
            request=request, template_name = 'home.html', context = {}
        )

# Page_for_Tags views should display industries that relate to the tag selected **Doesn't take in any info from the user**
class Page_for_TagsView(View):
    def get(self, request,tag_id):

        return render(
            request=request, template_name = 'Page_for_Tags.html', context = {}
        )
