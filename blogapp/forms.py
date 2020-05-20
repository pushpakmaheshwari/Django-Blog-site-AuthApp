from django import forms
from django.contrib.auth.models import User
from .models import Upload



class SignupForm(forms.ModelForm):
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'username', 'email', 'password')
        widgets = {'password':forms.PasswordInput()}


class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload
        fields = ('Title','Description','postedby','pic')
