from django.shortcuts import render
from django.views import View
from bizwiz.models import *

# Create your views here.

class Home(View):
    def get(self, request):

        return render(
            request=request, template_name = 'home.html', context = {}
        )

