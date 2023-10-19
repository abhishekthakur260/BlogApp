from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostModel
from .forms import PostModelForm
from django.core.paginator import Paginator

# Create your views here.
def Posts(request):
    post = PostModel.objects.all()
    posts_per_page = 10
    paginator = Paginator(post, posts_per_page)
    page = request.GET.get('page') 
    page_post = paginator.get_page(page)
     
    if request.method == 'POST':
        form = PostModelForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('posts-index')
    else:
        form = PostModelForm()
    
    context = {
        'form': form,
        'posts': post,
        'page_post':page_post,
   }
    return render(request,'blog/index.html',context)


