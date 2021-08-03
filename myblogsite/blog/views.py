from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Author, Post


def index(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')



def view_all_blogs(request):
    all_blogs = Post.objects.all().order_by('-date_publishshed')

    paginator = Paginator(all_blogs, 5) # Show 5 blogs per page.

    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    context = {
        'all_blogs' : page_obj,
    }

    return render(request, 'allBlogs.html', context)


def view_all_authors(request):
    all_bloggers = Author.objects.all()

    context = {
        'all_bloggers' : all_bloggers,
    }

    return render(request, 'allBloggers.html', context)



def view_blog(request, blog_id):
    blog = Post.objects.filter(id=blog_id).get()

    context = {
        'blog' : blog,
    }

    return render(request, 'blog.html', context)


def view_author(request, blogger_id):
    blogger = Author.objects.filter(id=blogger_id).get()
    blogs_by_blogger = Post.objects.filter(create_by=blogger_id).order_by('-date_publishshed')

    context = {
        'blogger' : blogger,
        'blogs_by_blogger' : blogs_by_blogger,
    }

    return render(request, 'blogger.html', context)