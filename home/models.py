from django.db import models

class newProject(models.Model):
  name = models.CharField(max_length = 255)
  description = models.TextField()
  image = models.ImageField(upload_to= 'project_images')
  created_at = models.DateTimeField(auto_now_add= True, null= True)
  
  def __str__(self):
    return self.name
  
  class Meta():
    ordering = ['-created_at']

class messages(models.Model):
  name = models.CharField(max_length= 255)
  email = models.EmailField()
  message = models.TextField()
    
  def __str__(self):
    return self.name


class blogPost(models.Model):
  title = models.CharField()
  created = models.DateField(auto_now_add=True)
  preface = models.TextField(null=True)
  body = models.TextField()
  topic_image = models.ImageField(null=True, upload_to='blog_images/')

  
  def __str__(self):
     return self.title
  
  class Meta():
    ordering = ['-created']

class related_images(models.Model):
    related_images = models.ForeignKey(blogPost, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='blog_images/')

    


