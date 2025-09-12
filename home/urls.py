from django.urls import path
from . import views

urlpatterns = [
  path('about/', views.about, name= 'about'),
  path('blog/', views.blog, name= 'blog'),
  path('blog/<int:id>/', views.blogpost, name='blogpost'),
  path('portfolio/', views.portfolio, name= 'portfolio'),
  path('contact/', views.contact, name= 'contact'),
  path('', views.home, name = 'home'),
  ]