from django.urls import path
from .import views

app_name = 'app'

urlpatterns = [
path('',views.MemberListview.as_view(), name='index'),
path('add_Member', views.MemberCreateView.as_view(),name='add_Member'),
]