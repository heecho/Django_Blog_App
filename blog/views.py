from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Comment
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# Create your views here.
def home(request):
	return HttpResponse("Welcome to my Blog Site!")

def index(request):
	blog_list = Blog.objects.all()[:20]
	template_hash = {'blog_list':blog_list}
	return render(request,'blog/index.html', template_hash)

def new(request):
	template_hash = {}
	return render(request,'blog/new.html',template_hash)

def create(request):
	blog = Blog(blog_title = request.POST['blog_title'], blog_content = request.POST['blog_content'], user_id = User.objects.all()[0])
	blog.save()
	return HttpResponseRedirect(reverse('show', args=(blog.id,)))
 	
def blog_show(request, blog_id):
	#blog = Blog.objects.get(pk=blog_id)
	blog = get_object_or_404(Blog, pk=blog_id)
	comment_list = blog.comment_set.all().order_by('-id')
	template_hash = {'comment_list':comment_list,'blog':blog}
	return render(request, 'blog/show.html',template_hash)
	

def blog_edit(request, blog_id):
	#blog = Blog.objects.get(pk=blog_id)
	blog = get_object_or_404(Blog, pk=blog_id)
	template_hash = {'blog': blog}
	return render(request, 'blog/edit.html',template_hash)

def blog_update(request, blog_id):
	#blog = Blog.objects.get(pk=blog_id)
	blog = get_object_or_404(Blog, pk=blog_id)
	blog.blog_title = request.POST['blog_title']
	blog.blog_content = request.POST['blog_content']
	blog.save()
	return HttpResponseRedirect(reverse('show', args=(blog.id,)))

def delete_blog(request, blog_id):
	#blog = Blog.objects.get(pk=blog_id)
	blog = get_object_or_404(Blog, pk=blog_id)
	blog.delete()
	return HttpResponseRedirect(reverse('index'))

def new_comment(request, blog_id):
	#blog = Blog.objects.get(pk=blog_id)
	blog = get_object_or_404(Blog, pk=blog_id)
	c = Comment()
	c.comment_content = request.POST['comment_content']
	c.blog_id = blog
	c.user_id = User.objects.all()[0]
	c.save()
	return HttpResponseRedirect(reverse('show', args=(blog.id,)))


