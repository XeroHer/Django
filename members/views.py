from django.http import HttpResponse
from django.template import loader

def home(request):
  context={'name':'Bikesh', 'course':'IT'}
  template = loader.get_template('home.html')
  return HttpResponse(template.render(context, request))

def about(request):
  template = loader.get_template('about.html')
  return HttpResponse(template.render())

def skills(request):
  template = loader.get_template('skills.html')
  return HttpResponse(template.render())

def project(request):
  template = loader.get_template('project.html')
  return HttpResponse(template.render())

def contact(request):
  template = loader.get_template('contact.html')
  return HttpResponse(template.render())
