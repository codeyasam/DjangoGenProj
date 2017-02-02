from django.conf.urls import urls
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm

urlpatterns = [
	url(r'^$', views.home, name="home"),
	url(r'^login/$', auth_views.login, 
		{'template_name': 'auth_app/login.html', 'authentication_form': LoginForm}, 
		name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/login'}),
	url(r'^home/$', views.home, name="home"),
]