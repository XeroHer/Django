from django.http import HttpResponse
from django.template import loader
from .models import Member

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
  if request.method=="POST":
    print("This is post")
  template = loader.get_template('contact.html')
  return HttpResponse(template.render(),request)

def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('detail.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())

def testing(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('template.html')
  context = {
     'firstname': 'Linus',
    'fruits': ['Apple', 'Banana', 'Cherry'],  
    'mymembers': mymembers, 
  }
  return HttpResponse(template.render(context, request))
    