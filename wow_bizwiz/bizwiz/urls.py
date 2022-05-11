from django.urls import path
from bizwiz.views import * 

urlpatterns = [
 path('', HomeView.as_view(), name='home'),
 path('<int:tag_id>', Page_for_TagsView.as_view(), name='page_for_tags'),
 path('industry/<int:industry_id>', IndustryView.as_view(), name='industry')
]