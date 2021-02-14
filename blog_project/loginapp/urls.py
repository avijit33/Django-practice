from django.urls import path
from . import views

app_name = 'loginapp'

urlpatterns = [
    path('signup/', views.signup, name= "signup"),
    path('login/', views.login_page, name= "login"),
    path('logout/', views.logout_user, name= "logout"),
    path('profile/', views.profile, name= "profile"),
    path('profile-change/', views.profile_change, name= "profile_change"),
    path('password/', views.password_change, name= "password_change"),
    path('add-picture/', views.add_profile_pic, name= "add_profile_pic"),
    path('change-picture/', views.change_pro_pic, name= "change_pic"),
]
