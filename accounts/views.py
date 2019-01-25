from django.shortcuts import render, redirect

def login(request):
    return render(request, 'accounts/login.html', {})

def signup(request):
    return render(request, 'accounts/signup.html', {})

def forgotpassword(request):
    return render(request, 'accounts/forgotpassword.html', {})

def logout(request):
    return redirect('index')
