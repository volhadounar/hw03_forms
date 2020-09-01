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
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            new = Post(text=form.cleaned_data['text'], author=request.user,
                       group=form.cleaned_data['group'])
            new.save()
            return redirect('/')
        return render(request, 'newpost.html', {'form': form})
    form = PostForm()
    return render(request, 'newpost.html', {'form': form})