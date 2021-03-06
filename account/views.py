from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, CustomUser
from .forms import PostForm, SigninForm, UserForm

#from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.http import HttpResponse

# Create your views here.
def main(request):
    posts = Post.objects.all()
    signin_form = SigninForm()
    return render(request, 'signin.html', {'posts': posts, 'singin_form': signin})

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('main') ###########
        else:
            return HttpResponse("로그인 실패. 다시 시도해보세요")
    else:
        signin_form = SigninForm()
        return render(request, 'signin.html', {'signin_form': signin_form})
def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            new_user = CustomUser.objects.create_user(username=form.cleaned_data['username'],
            email=form.cleaned_data['email'],
            password=form.cleaned_data['password'],
            phone_number=form.cleaned_data['phone_number'])
            login(request, new_user)
            return redirect('main')
        else:
            return redirect('main')
    else:
        form = UserForm()
        return render(request, 'signup.html', {'form': form})
