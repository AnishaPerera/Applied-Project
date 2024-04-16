from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserSignUpForm, UserUpdateForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash

# Create your views here.

def register(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            form = UserSignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                messages.success(request, f'Your Account is Created, Please Log In !!')
                return redirect('signin')
        else:
            form = UserSignUpForm()
        return render(request, 'users/signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        userform= UserUpdateForm(request.POST, instance=request.user)
        
        if userform.is_valid():
            userform.save()
            messages.success(request, f'Your Account Details are Updated !!')
            return redirect('profile')

    else:
        userform= UserUpdateForm(instance=request.user)
                

    context = {
        'userform': userform,
    }

    return render(request, 'users/profile.html', context)


def change_password(request):
    if request.method == 'POST':
        form= PasswordChangeForm(request.user, request.POST)
        
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your Password has been Updated !!')
            return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'users/change_password.html', {'form': form})
