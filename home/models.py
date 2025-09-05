from django.db import models

class newProject(models.Model):
  name = models.CharField(max_length = 255)
  description = models.TextField()
  image = models.ImageField(upload_to= 'project_images')
  
  def __str__(self):
    return self.name
