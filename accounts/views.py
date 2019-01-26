from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
import sys

def login(request):
    if request.method == 'POST':
        # Get form values
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(username=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials.')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html', {})

def signup(request):

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check for password criteria
        if password != confirm_password:
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already used to make an account with us.')
            return redirect('signup')
        elif len(password) < 8:
            messages.error(request, 'Passwords must be at least 8 characters long.')
            return redirect('signup')
        elif password.isupper() or password.islower():
            messages.error(request, 'Passwords must contain both uppercase and lowercase characters.')
            return redirect('signup')

        else:
            messages.error(request, 'Signup worked! You can now login.')
            # Create User
            user = User.objects.create_user(first_name=first_name, last_name=last_name, 
                                            email=email, username=email, password=password)
            user.save()
            # Redirect user to login page if signup works
            return redirect('login')
    else:
        return render(request, 'accounts/signup.html', {})

def forgotpassword(request):
    return render(request, 'accounts/forgotpassword.html', {})

def logout(request):
    auth.logout(request)
    return redirect('index')
