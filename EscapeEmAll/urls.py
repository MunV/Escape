from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic.base import TemplateView 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/',  include('django.contrib.auth.urls') ),
    url(r'^', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^index',  include ('rooms.urls')),
]
