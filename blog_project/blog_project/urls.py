from django.contrib import admin
from django.urls import path, include
from blog_project import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('loginapp.urls')),
    path('blog/', include('blogapp.urls')),
    path('', views.index , name="index"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
