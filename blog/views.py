# Create your views here.
from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from blog.models import BlogPost
from operator import attrgetter
from django.db.models  import Q
from blog.forms import CreateBlogPostForm, UpdateBlogPostForm
from account.models import Account
from django.contrib import messages
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.contrib import admin

BLOG_POSTS_PER_PAGE = 3

def get_blog_queryset(query=None):
	queryset = []
	queries = query.split(" ")
	for q in queries:
		posts = BlogPost.objects.filter(
			Q(title__contains=q)|
			Q(body__icontains=q)
			).distinct()
		for post in posts:
			queryset.append(post)

	# create unique set and then convert to list
	return list(set(queryset))



def home(request, *args, **kwargs):
    context = {}

    #search
    query = ""
    if request.GET:
        query = request.GET.get('q','')
        context['query'] = str(query)

    blog_posts = sorted(get_blog_queryset(query), key=attrgetter('date_updated'), reverse=True)

    #pagination
    page = request.GET.get('page', 1)
    blog_posts_paginator = Paginator(blog_posts, BLOG_POSTS_PER_PAGE)
    try:
        blog_posts = blog_posts_paginator.page(page)
    except PageNotAnInteger:
        blog_posts = blog_posts_paginator.page(BLOG_POSTS_PER_PAGE)
    except EmptyPage:
        blog_posts = blog_posts_paginator.page(blog_posts_paginator.num_pages)

    context['blog_posts'] = blog_posts

    return render(request, "blog/index.html", context)



def create_blog(request):
 
    context = {}

    user = request.user
    if not user.is_authenticated:
        
            return redirect('must_authenticate')

    
    form = CreateBlogPostForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        author = Account.objects.filter(email=user.email).first()
        obj.author = author
        obj.save()
        form = CreateBlogPostForm()
        messages.success(request, 'Blog Posted')

    context['form'] = form
    
    return render(request,"blog/create_blog.html",context)

def detail_blog_view(request, slug):
	
    blog_post = []
    blog_post = get_object_or_404(BlogPost, slug=slug)
    
    
    context = {
        'blog_post':blog_post 
    }

    return render(request, 'blog/detail_blog.html', context)

def edit_blog_view(request, slug):
    context = {}

    user = request.user
    if not user.is_authenticated:
        return redirect("must_authenticate")

    blog_post = get_object_or_404(BlogPost, slug=slug)
    if blog_post.author != user:
        return HttpResponse('You are not the author of that post.')
    if request.POST:
        form = UpdateBlogPostForm(request.POST or None, request.FILES or None, instance = blog_post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.success(request, 'your blog has been Updated')
            blog_post = obj
    form = UpdateBlogPostForm(
        initial={
            'title':blog_post.title,
            'body':blog_post.body,
            'image':blog_post.image,
        }
    )

    context['form'] = form
    return render(request, 'blog/edit_blog.html',context)



def get_blog_query(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        posts = BlogPost.objects.filter(
            Q(title_icontains=q),
            Q(body_icontains=q)
        ).distinct()

    
        for post in posts:
            queryset.append(post)

    return list(set(queryset))


