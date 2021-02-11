from django.shortcuts import get_object_or_404, render
from . models import Group, Post
from . forms import PostForm
from django.shortcuts import redirect


def index(request):
    posts = Post.objects.all()[:10]
    return render(request, 'index.html', {'posts': posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)

    posts = group.posts.all()[:12]
    return render(request, 'group.html', {'group': group, 'posts': posts})


def new_post(request):
    if request.method != 'POST':
        form = PostForm()
        return render(request, 'newpost.html', {'form': form})
    if not request.user.is_authenticated:
        return redirect('login')
    form = PostForm(request.POST)
    if form.is_valid() is False:
        return render(request, 'newpost.html', {'form': form})
    new_item = form.save(commit=False)
    new_item.author = request.user
    new_item.save()
    return redirect('index')
