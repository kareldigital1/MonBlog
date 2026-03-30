from django.shortcuts import render , redirect
from .form import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from django.contrib import messages


# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

# view pour l'inscription des utilisateurs
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login_view')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# view pour la connexion des utilisateurs
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login_view.html') 

def logout_view(request):
    logout(request)
    return redirect('login_view')