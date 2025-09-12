from django.contrib import admin
from .models import newProject, messages, blogPost, related_images
admin.site.register(newProject)
admin.site.register(messages)

class related_imagesInline(admin.StackedInline):
    model =  related_images
    extra = 1

class blogPostAdmin(admin.ModelAdmin):
    inlines = [related_imagesInline]

admin.site.register(blogPost, blogPostAdmin)