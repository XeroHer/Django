from django.http import HttpResponse
from django.template import loader
from .models import Member
from .models import Contact

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
    first = request.POST.get("firstname")
    last = request.POST.get("lastname")
    country = request.POST.get("country")
    subject = request.POST.get("subject")
    # Save to database
    sav=Contact(
            firstname=first,
            lastname=last,
            country=country,
            subject=subject
        )
    sav.save()
  print("Form submitted and data saved.")
  template = loader.get_template('contact.html')
  context={}
  return HttpResponse(template.render(context,request))

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
  # mydata = Member.objects.all().values()
  # SQL=SELECT * FROM members WHERE firstname = 'Emil';
  # mydata = Member.objects.filter(lastname='Refsnes', id=2).values()
  # SQL=SELECT * FROM members WHERE lastname = 'Refsnes' AND id = 2;
  # mydata = Member.objects.filter(firstname='Emil').values() | Member.objects.filter(firstname='Tobias').values()
  # SQL=SELECT * FROM members WHERE firstname = 'Emil' OR firstname = 'Tobias';
  # mydata = Member.objects.values_list('firstname')
  # mymembers = Member.objects.all().values()



  # Use the __startswith keyword:
  # .filter(firstname__startswith='L');
  # SQL WHERE firstname LIKE 'L%'
  # mydata = Member.objects.filter(firstname__startswith='L').values()



# Order the result alphabetically by firstname:uses the order_by() method:
# mydata = Member.objects.all().order_by('firstname').values()
# SELECT * FROM members ORDER BY firstname;

# Order the result firstname descending:
# mydata = Member.objects.all().order_by('-firstname').values()
# SELECT * FROM members ORDER BY firstname DESC;

# Order the result first by lastname ascending, then descending on id:
# mydata = Member.objects.all().order_by('lastname', '-id').values()
# SELECT * FROM members ORDER BY lastname ASC, id DESC;


  mydata = Member.objects.filter(firstname='Emil').values()
  template = loader.get_template('template.html')
  context = {
     'firstname': 'Linus',
    'fruits': ['Apple', 'Banana', 'Cherry'],  
    # 'mymembers': mymembers, 
    'mymembers': mydata,
  }
  return HttpResponse(template.render(context, request))
    