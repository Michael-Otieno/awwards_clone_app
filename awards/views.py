from django import template
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from awards.models import Comment, Like, Project
from .forms import SignUpForm, PostProjectForm, ProfileForm,Profile
from django.contrib.auth.models import User
from django.template import context, loader
from django.contrib.auth import login, authenticate
from django.urls import reverse


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
    projects = Project.objects.filter(author_user_username=request.user.username)

    context ={'profile':profile, 'projects':projects}
    return HttpResponse(template.render(context, request))

     
def add_comment(request):
    if request.POST:
        description, id = request.POST['description'], request.POST['demo']
        projects = Project.objects.get(pk=id)
        if description is not None:
            Comment.objects.create(projects=projects, description=description, user=request.user)
            return redirect(reverse('home'))

def like_project(request, projectid):
    project = Project.objects.get(id=projectid)
    try:
        is_Liked = Like.objects.get(project_linked=project, user__username=request.user.username)
        Like.objects.filter(project_linked=project, user__username=request.user.username).delete()
        project.likes -=1

    except Like.DoesNotExist:
        Like.objects.create(project_linked=project, user=request.user)
        project.likes +=1

    project.save()
    return redirect(reverse('home'))

def add_project(request):
    template = loader.get_template('award/project.html')
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        form = PostProjectForm(request.POST, request.FILES)

        if form.is_valid():
            fs = form.save(commit=False)
            fs.author = profile
            fs.save()
            return redirect(reverse('home'))

    else:
        form = PostProjectForm()
        pass

    context={'form':form, 'profile':profile}
    return HttpResponse(template.render(context, request))

def edit_profile(request, username):
    template = loader.get_template('award/edit_profile.html')
    user = User.objects.get(username=request.user.username)
    profile = Profile.objects.get(user=request.user)

    if request.meyhod == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.save()
            profile.biography = form.cleaned_data['biography']
            profile.profile_pic = form.cleaned_data['profile_pic']
            profile.contact = form.cleaned_data['contact']
            profile.save()
            return redirect(reverse('home'))

    else:
        form = ProfileForm(initial={
                                    'username': username,
                                    'first_name': user.first_name,
                                    'last_name': user.last_name,
                                    'email':user.email,
                                    'biography': profile.biography})

    context = {'form':form, 'user':user, 'profile':profile}
    return HttpResponse(template.render(context, request))

def search_project(request):
    if 'search_project' in request.GET and request.GET['search_project']:
        title = request.GET.get('search_project')
        results = Project.search_project(title)
        print(results)
        message = f'title'
        params = {
            'results':results,
            'message':message
        }
        return render(request, 'award/result.html', params)

    else:
        message='Project not found'

    return render(request, 'award/result.html', {'message':message})



    