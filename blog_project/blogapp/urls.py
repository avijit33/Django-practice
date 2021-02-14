from django.urls import path
from blogapp import views

app_name = 'blogapp'

urlpatterns = [
    path('', views.BlogList.as_view() , name="blog_list"),
    path('create/',  views.CreateBlog.as_view() , name="create_blog"),
    path('details/<slug:slug>', views.blog_details, name="blog_details"),
    path('liked/<pk>', views.liked, name= "like_post"),
    path('unliked/<pk>', views.unliked, name= "unlike_post"),
    path('my-blog/', views.MyBlog.as_view(), name= "my_blog"),
    path('edit/<pk>', views.UpdateBlog.as_view(), name= "edit_blog"),
    path('about/', views.ShowProfile.as_view(), name= "about_profile"),
]
