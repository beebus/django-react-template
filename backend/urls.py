from django.urls import path, include, re_path as url
from django.contrib.auth.views import LogoutView, LoginView
from django.contrib import admin
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .views import app, index

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include('users.urls')),
    url(r'^app/', app, name='app'),
    url('^auth/login/$', LoginView.as_view(template_name='auth/login.html'), name='login'),
    url('^auth/logout/$', LogoutView.as_view(next_page=reverse_lazy('login')), name='logout'),
    url('^$', index, name='index'),
    path('app/', TemplateView.as_view(template_name="index.html"), name="app"),
]
