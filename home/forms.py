from django import forms
from .models import messages

class contactForm(forms.ModelForm):
  class Meta():
    model = messages
    fields =  ('name', 'email', 'message',)
    widgets = {
      'name':forms.TextInput(attrs={
      'placeholder': 'Your name',
      'class': 'form_field',
        }),
      'email': forms.EmailInput(attrs={
            'placeholder': 'Your Email',
            'class': 'form_field',
        }),
      'message': forms.Textarea(attrs={
            'placeholder': 'Your message',
            'class': 'form_field',
        }),
    }
