from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def login(request):
    return render(request, 'accounts/login.html', {})

def signup(request):

    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm-password']

        # Check if password match
        if password != confirm_password:
            print('Passwords do not match.')
            messages.error(request, 'Passwords do not match.')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            print('Email already exists.')
            return redirect('signup')
        elif len(password) < 8:
            print('Passwords must be at least 8 characters.')
            return redirect('signup')
        else:
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
    return redirect('index')
