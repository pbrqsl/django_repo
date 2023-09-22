from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
# Create your views here.

class CustomLoginView(LoginView):
    class Meta:
        model = CustomUser
        fields = ['email']


class CustomProfile(DetailView):
    class Meta:
        model = CustomUser


def register(request):
    if request.method == "POST":
        # return HttpResponse('aaa')
        form = CustomUserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account creatred for user {email}.')
            return render(request, 'users/post_register.html', {'email': email})
        else:
            return HttpResponse('invalid form')
            
    else:
        form = CustomUserCreationForm()
        return render(request, 'users/register.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'users/dashboard.html')