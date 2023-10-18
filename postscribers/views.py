from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PostModel
from .forms import PostModelForm

# Create your views here.
def Posts(request):
    post = PostModel.objects.all()
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
   }
    return render(request,'blog/index.html',context)


