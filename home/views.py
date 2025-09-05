from django.shortcuts import render
from .models import newProject

def home(request):
  return render(request, 'index.html')
  
def about(request):
  return render(request, 'about.html')
  
def blog(request):
  return render(request, 'blog.html')
  
def portfolio(request):
  newproject = newProject.objects.all()
  return render(request, 'portfolio.html', {
      'newproject': newproject,
  })
  
def contact(request):
  return render(request, 'contact.html')