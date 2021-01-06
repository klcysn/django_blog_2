from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm

# Create your views here.

def post_list(request):
    qs = Post.objects.filter(status="published")
    context = {
        "object_list" : qs
    }
    return render(request, "blog/post_list.html", context)

def post_create(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.save()
            return redirect("blog:post-list")
    context ={
        "form" : form
    }
    
    return render(request, "blog/post_create.html", context)


def post_detail(request, slug):
    obj = get_object_or_404(Post, slug=slug)
    context = {
        "object": obj
    }
    return render(request, "blog/post_detail.html", context)