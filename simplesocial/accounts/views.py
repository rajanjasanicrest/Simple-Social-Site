from django.shortcuts import render ,redirect
from django.urls import reverse_lazy,reverse
from . import forms
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import UserLoginForm
# Create your views here.
class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'


@login_required
def logout1(request):
    logout(request)
    return redirect('thanks')

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username,password=password)
        if user:
            login(request, user)
            return redirect( reverse('posts:all') )
        else:
            messages.add_message(request, messages.ERROR, "Invalid Credentials!")
            return redirect('login')
    else:
        form = UserLoginForm()
        return render(request, 'accounts/login.html',{'form':form})