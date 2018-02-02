from django.conf.urls import include, url
from django.contrib import admin

from django.contrib.auth import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/login/$', views.login, {'template_name': 'admin/login.html'}, name='login'),
    url(r'', include('blog.urls')),
]