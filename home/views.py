from django.shortcuts import render, redirect, get_object_or_404
from .models import newProject, messages, blogPost
from .forms import contactForm

def home(request):
  return render(request, 'index.html')
  
def about(request):
  return render(request, 'about.html')
  
def blog(request):
  blog_post = blogPost.objects.all()
  return render(request, 'blog.html', {
    'post': blog_post
  })
  
def portfolio(request):
  newproject = newProject.objects.all()
  return render(request, 'portfolio.html', {
      'newproject': newproject,
  })
  
def contact(request):
  form = contactForm()
  if request.method == 'POST':
    form = contactForm(request.POST)

    if form.is_valid():
      message = form.save()
      return redirect('contact')
    else:
      print(form.errors)
  return render(request, 'contact.html', {'form': form})

def blogpost(request, id):
  blog_post = get_object_or_404(blogPost, id=id)
  return render(request, 'blogpost.html', {
    'post': blog_post,
  })