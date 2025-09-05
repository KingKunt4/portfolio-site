from django.urls import path
from . import views

urlpatterns = [
  path('about/', views.about, name= 'about'),
  path('blog/', views.blog, name= 'blog'),
  path('portfolio/', views.portfolio, name= 'portfolio'),
  path('contact/', views.contact, name= 'contact'),
  path('', views.home, name = 'home'),
  ]