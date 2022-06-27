from django.shortcuts import render, redirect, get_object_or_404
from content.models import Portfolio, Profile
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from content.forms import AddPortfolioform, UpdateProfileForm, UpdateUserForm

# Create your views here.
def loginUser(request):
  if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = authenticate(username=username, password=password)

      if not User.objects.filter(username=username).exists():
          messages.error(request, 'Username Does Not Exist! Choose Another One.')
          return redirect('login')

      if user is None:
        messages.error(request, 'Username/Password Is Incorrect! Please Try Again')
        return redirect('login')

      if user is not None:
        login(request, user)
        return redirect(reverse('portfolio'))
  return render(request, 'login.html')

def signup(request):
  if request.method == 'POST':
        context = {'has_error': False}
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, 'Passwords Do Not Match! Try Again')
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Already Exists! Choose Another One')
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Address Already Exists! Choose Another One')
            return redirect('signup')

        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password1)
        user.save()        
  
  return render(request, 'signup.html')

@login_required(login_url='login')
def logoutUser(request):
  logout(request)
  messages.success(request, 'Succesfully Logged Out')
  return redirect('login')

def index(request):
  return render(request, 'index.html')

@login_required(login_url='login')
def portfolio(request):
   posts = Portfolio.objects.order_by('-date_created').all()
   profiles = Profile.objects.all()
   return render(request, 'portfolio.html', {'posts':posts, 'profiles':profiles})

@login_required(login_url='login')
def MyProfile(request, username):
    profile = User.objects.get(username=username)
    profile_details = Profile.objects.get(user = profile.id)
    images = Portfolio.objects.filter(user = profile.id).all()
    images_count = Portfolio.objects.filter(user = profile.id)
    
    return render(request, 'my_profile.html', {'profile':profile, 'profile_details':profile_details, 'images':images, 'images_count':images_count,})

@login_required(login_url='login')
def UserProfile(request, username):
  current_user = request.user
  profile = User.objects.get(username=username)
  profile_details = Profile.objects.get(user = profile.id)
  images = Portfolio.objects.filter(user = profile.id).all()
  images_count = Portfolio.objects.filter(user = profile.id)

  return render(request, 'user_profile.html', {'profile':profile, 'profile_details':profile_details, 'images':images, 'images_count':images_count, 'current_user':current_user})

@login_required(login_url='login')
def add_portfolio(request):
    # profile = User.objects.get(username=username)
    # profile_details = Profile.objects.get(user=profile.id)
    form = AddPortfolioform()
    if request.method == 'POST':
        form = AddPortfolioform(request.POST, request.FILES)
        if form.is_valid():
            portfolio = form.save(commit=False)
            portfolio.user = request.user
            portfolio.profile = request.user.profile
            portfolio.save()
            messages.success(request, 'Your Portfolio Was Added Successfully!')
            return redirect('add_portfolio')
        else:
            messages.error(request, "Your Portfolio Wasn't Created!")
            return redirect('add_portfolio')
    else:
        form = AddPortfolioform()
    return render(request, 'add_portfolio.html', {'form':form, })

@login_required(login_url='Login')
def EditProfile(request, username):
    user = User.objects.get(username=username)
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your Profile Has Been Updated Successfully!')
            return redirect('my_profile', username=username)
        else:
            messages.error(request, "Your profile Wasn't Updated!")
            return redirect('EditProfile', username=username)
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})

def Search(request):
    current_user = request.user
    if request.method == 'POST':
        search = request.POST['portfolioSearch']
        users = User.objects.filter(username__icontains = search).all()
        if not users:
            return render(request, 'search_results.html', {'search':search, 'users':users})
        else:
            images = Portfolio.objects.filter(user = users[0]).all()
            images_count = Portfolio.objects.filter(user = users[0])
            
            
            return render(request, 'search_results.html', {'search':search, 'users':users, 'images':images, 'images_count':images_count, 'current_user':current_user,})
    else:
        return render(request, 'search_results.html')
    
# @login_required(login_url='login')
def Settings(request):
    # profile = User.objects.get(username=username)
    # username = User.objects.get(username=username)
    # if request.method == "POST":
    #     form = PasswordChangeForm(data=request.POST, user=request.user)
    #     if form.is_valid():
    #         form.save()
    #         update_session_auth_hash(request, form.user)
    #         messages.success(request, 'Your Password Has Been Updated Successfully!')
    #         return redirect("my_profile", username=username)
    #     else:
    #         messages.error(request, "Your Password Wasn't Updated!")
    #         return redirect("Settings", username=username)
    # else:
    #     form = PasswordChangeForm(data=request.POST, user=request.user)
    # {'form': form}
    return render(request, "settings.html")
