from django import forms
from .models import Image, Profile, Comments 
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude = ['likes','profile']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
