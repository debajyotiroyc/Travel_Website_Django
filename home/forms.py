from django import forms
from django.contrib.auth.models import User
from home.models import profile

class ProfileForm(forms.ModelForm):
    #username=forms.CharField(widget=forms.CharField)
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','password')

class infoprofileform(forms.ModelForm):
    class Meta():
        model=profile
        fields = ('Country', 'State')
