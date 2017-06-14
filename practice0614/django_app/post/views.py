from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }

    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExitst as e:
        return HttpResponse('페이지를 찾을 수 없습니다.')
    context = {
        'post': post
    }
    return render(request, 'post/post_detail.html', context)


def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')

