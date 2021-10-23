from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import SignUpForm, PostProjectForm, ProfileForm,Profile
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=username,
                                            password=password,
                                            first_name=first_name,
                                            last_name=last_name,
                                            email=email)
            profile = Profile.objects.create(user=user)

            return HttpResponseRedirect('/accounts/login')

    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})

