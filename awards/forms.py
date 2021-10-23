from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Project
# from pyuploadcare.dj.forms import ImageField
from django.forms import ModelForm



class SignUpForm(forms.Form):
    username = forms.CharField(max_length=30,required=True,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"Username"},))
    first_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"First Name"}))
    last_name = forms.CharField(max_length=30, required=False,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"Last Name"}))
    email = forms.EmailField(max_length=254,widget=forms.TextInput(attrs={'class':'input-fields','placeholder':"Email"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input-fields','placeholder':"Password"}),required=True)


class PostProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description','url']


class ProfileForm(forms.Form):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ""  # Removes : as label suffix

    profile_pic = forms.ImageField(required=False)
    username = forms.CharField(max_length=500,required=True)
    first_name = forms.CharField(max_length=500, required=False)
    last_name = forms.CharField(max_length=500, required=False)
    biography = forms.CharField(required=False, widget=forms.Textarea())
