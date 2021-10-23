from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from awards.models import Project
from .forms import SignUpForm, PostProjectForm, ProfileForm,Profile
from django.contrib.auth.models import User
from django.template import context, loader
from django.contrib.auth import login, authenticate



# Create your views here.
# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             first_name = form.cleaned_data['first_name']
#             last_name = form.cleaned_data['last_name']
#             email = form.cleaned_data['email']
#             password = form.cleaned_data['password']

#             user = User.objects.create_user(username=username,
#                                             password=password,
#                                             first_name=first_name,
#                                             last_name=last_name,
#                                             email=email)
#             profile = Profile.objects.create(user=user)

#             return HttpResponseRedirect('/accounts/login')

#     else:
#         form = SignUpForm()

#     return render(request, 'registration/signup.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email)
        
        user.save()
        profile = Profile.objects.create(user=user)

        return HttpResponseRedirect('/accounts/login')

    else:
        return render(request, 'registration/signup.html')







def home(request):
    # template = loader.get_template('award/home.html')
    # if request.user.is_anonymous:
    #     context = {}
    #     return HttpResponse(template.render(context, request))
    projects=Project.objects.all()
    return render(request, 'award/home.html',{'project':projects})

def login_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse('user logged in')
    
    else:
        return HttpResponse('user not logged in')

def user_profile(request, username):
    template=loader.get_template('award/profile.html')
    profile = Profile.objects.get(user=request.user)
    posts = Project.objects.filter(author_user_username=request.user.username)

    context ={'profile':profile, 'post':posts}
    return HttpResponse(template.render(context, request))

     

