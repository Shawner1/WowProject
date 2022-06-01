from django.urls import path
from bizwiz.views import * 
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
 path('', views.homee, name="homee"),
 path('signup', views.signup, name="signup"),
 path('signin', views.signin, name="signin"),
 path('signout', views.signout, name="signout"),
 path('', HomeView.as_view(), name='home'),
 path('industry/<int:industry_id>/', IndustryView.as_view(), name='industry'),
 path('question/<int:industry_id>/<int:question_id>/', Specific_QuestionView.as_view(), name= 'specific_question'),
 path('tags/<int:tag_id>/', Page_for_TagsView.as_view(), name='page_for_tags'),
 path('updating_page/<int:industry_id>/<int:question_id>/<int:answer_id>/', Updating_PageView.as_view(), name='updating_page')
]