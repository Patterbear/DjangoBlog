from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()  # saves form data to new user
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


# Django decorator that makes being logged in required to access URL
# Does this by redirecting user to login page if they're not already logged in
# After login, redirects user to the page they were originally trying to access
@login_required
def profile(request):
    return render(request, 'users/profile.html')
