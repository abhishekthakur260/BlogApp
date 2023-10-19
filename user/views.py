from django.shortcuts import render, redirect
from .forms import SignUpForm
# Create your views here.

def sign_up(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts-index')    
    else:
        form = SignUpForm()
            
    context = {
        'form': form,
    }
    
    return render(request,'signup/sign_up.html', context)


def profile(request):
    return render(request,'signup/profile.html')