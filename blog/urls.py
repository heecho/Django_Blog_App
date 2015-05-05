from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples: /blogs
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^new$', 'blog.views.new', name='new'),
    url(r'^create$', 'blog.views.create', name='create'),
    url(r'^(?P<blog_id>[0-9]+)/?$', 'blog.views.blog_show', name='show'),
    url(r'^(?P<blog_id>[0-9]+)/edit$', 'blog.views.blog_edit', name='edit'),
    url(r'^(?P<blog_id>[0-9]+)/update$', 'blog.views.blog_update', name='update'),
    url(r'^(?P<blog_id>[0-9]+)/delete$', 'blog.views.delete_blog', name='delete'),
	url(r'^(?P<blog_id>[0-9]+)/new_comment$', 'blog.views.new_comment', name='comment'),
    # url(r'^blog/', include('blog.urls')),


]
