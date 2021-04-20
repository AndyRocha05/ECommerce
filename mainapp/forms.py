# forms.py 
from django import forms 
from mainapp.models import Image
  
class ImgForm(forms.ModelForm): 
  
    class Meta: 
        model = Image 
        fields = ['name', 'img', 'product'] 