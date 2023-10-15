
from django.urls import path 
from . import views

app_name = 'jobs'
urlpatterns = [
    path('', views.job_list , name='job_list'),
    path('add', views.job_add, name='job_add'),
    path('<str:slug>', views.job_detail, name='job_detail'),
    
]
