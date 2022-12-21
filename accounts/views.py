from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.

def index(request):
    return render(request,'base.html')

def login(request):
    pass

def register(request):
    if request.method == 'POST':
        form_obj = UserCreationForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            un=form_obj.cleaned_data.get('username')
            messages.success(request,f' Congrates {un},your a/c has been create successfully ' )
            return redirect('login_url')
    else:
        form_obj = UserCreationForm()
        return render(request,
                      'accounts/register.html',
                      {'form':form_obj}
                      )
