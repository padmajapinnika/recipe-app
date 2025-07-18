from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def home(request):
  return redirect('login')

def login_view(request):
  error_message = None
  form = AuthenticationForm()

  if request.method == 'POST':
    form = AuthenticationForm(data = request.POST)
    if form.is_valid():
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password')
      user = authenticate(username = username, password = password)
      if user is not None:
        login(request, user)
        return redirect('recipes:home')
    else:
      error_message = 'oops... something went wrong'
  context = {
    'form': form,
    'error_message': error_message
  }

  return render(request, 'auth/home.html', context)



def logout_view(request):
    logout(request)
    return redirect('recipes:login')  # or any other page like 'home'
