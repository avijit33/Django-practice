from django.conf.urls import url 
from django.urls import path 
from loginapp import views

app_name = "loginapp"

urlpatterns = [
   path('', views.index, name = 'index'),
   path('register/', views.register, name = 'register'),
   path('login/', views.login_page, name = 'login'),
   path('user-login/', views.login_user, name = 'login_user'),
   path('user-logout/', views.user_logout, name = 'logout'),
]
