from content import views
from django.urls import re_path, path

urlpatterns = [
  path('login', views.loginUser, name='login'),
  path('', views.index, name='index'),
  path('signup', views.signup, name='signup'),
  path('logout/', views.logoutUser, name='logout'),
  re_path(r'^profile/(?P<username>\w{0,50})/$', views.MyProfile, name = 'my_profile'),
  re_path(r'^user/(?P<username>\w{0,50})/$', views.user_profile, name="user_profile"),
  re_path(r'^profile/(?P<username>\w{0,50})/edit/$', views.EditProfile, name="EditProfile"),
  re_path(r'^search-results/$', views.Search, name="search_results"),
  re_path(r'^profile/(?P<username>\w{0,50})/image/add/$', views.add_portfolio, name="add_portfolio"), 
]

