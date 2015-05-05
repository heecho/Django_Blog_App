from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^blogs/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
