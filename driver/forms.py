from django import forms 
from .models import *



class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['full_name','email', 'address']





class UploadForm(forms.ModelForm):
    
    screenshot = forms.ImageField(label='upload an image')
    
    class Meta:
      model = Upload
      fields = ['screenshot']


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ['name','email', 'subject','message']