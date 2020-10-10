from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('home', views.index, name='home'),
    path('overview', views.overview, name='overview'),
    path('skills', views.skills, name='skills'),
    path('about', views.about, name='about'),
]