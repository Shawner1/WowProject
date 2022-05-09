from django.shortcuts import render
from django.views import View
from bizwiz.models import *

# Create your views here.

# Home page views it should display industries and tags **Doesn't take in any info from the user**
class Home(View):
    def get(self, request):

        return render(
            request=request, template_name = 'home.html', context = {}
        )

