from django import forms

class contactForm(forms.Form):
  name = forms.CharField(label = 'name:', widget= forms.TextInput(attrs= {
    'maxlength': 200,
    'class': 'contactform',
  }))
  email = forms.EmailField()