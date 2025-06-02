from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('skills/', views.skills, name='skills'),
    path('project/', views.project, name='project'),
    path('contact/', views.contact, name='contact'),

]