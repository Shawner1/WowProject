from django.urls import path
from bizwiz.views import * 
from django.urls import path
from bizwiz.views import * 
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import LikeView

urlpatterns = [
 path('', views.registerPage, name='register'),
 path('home/', HomeView.as_view(), name='home'),
 path('industries/', IndustriesView.as_view(), name='industries'),
 path('signin/', views.signin, name='signin'),
 path('signout/', views.signout, name='signout'),
 path('industry/<int:industry_id>/', IndustryView.as_view(), name='industry'),
 path('question/<int:industry_id>/<int:question_id>/', Specific_QuestionView.as_view(), name= 'specific_question'),
 path('tags/<int:tag_id>/', Page_for_TagsView.as_view(), name='page_for_tags'),
 path('updating_page/<int:industry_id>/<int:question_id>/<int:answer_id>/', Updating_PageView.as_view(), name='updating_page'),
 path('like/<int:industry_id>/<int:question_id>/<int:answer_id>/', LikeView, name='like_post'),
 path('userprofile/<int:user_id>/', ProfileView.as_view(), name='profile_page')
]