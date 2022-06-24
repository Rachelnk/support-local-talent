from django.shortcuts import render, redirect, get_object_or_404
from content.models import Portfolio, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from content.forms import AddPortflioform, UpdateProfileForm, UpdateUserForm

# Create your views here.
# def loginUser(request):
#   if request.method == 'POST':
#       username = request.POST['username']
#       password = request.POST['password']
#       user = authenticate(username=username, password=password)

#       if not User.objects.filter(username=username).exists():
#           messages.error(request, 'Username Does Not Exist! Choose Another One.')
#           return redirect('login')

#       if user is None:
#         messages.error(request, 'Username/Password Is Incorrect! Please Try Again')
#         return redirect('login')

#       if user is not None:
#         login(request, user)
#         return redirect(reverse('index'))
#   return render(request, 'login.html')

@login_required(login_url='login')
def logoutUser(request):
  logout(request)
  messages.success(request, 'Succesfully Logged Out')
  return redirect('login')


def index(request):
  
  return render (request, 'index.html', {})
# Create your views here.
