from .models import CustomUser, LoginHistory
from .forms import CustomUserCreationForm, CustomPasswordResetForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetDoneView
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Max
from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.core.mail import send_mail
# Create your views here.

class CustomLoginView(LoginView):
    #send_mail('test_subject', 'test_message', 'django@a.pl', ['a1@b.pl'])
    class Meta:
        model = CustomUser
        fields = ['email']


class CustomProfile(DetailView):
    class Meta:
        model = CustomUser

class CustomPasswordReset(PasswordResetView):
    template_name = 'users/password_reset.html'
    form_class = CustomPasswordResetForm
    

    class Meta:
        model = CustomUser

class CustomPasswordResetDone(PasswordResetDoneView):
    template_name= 'users/password_reset_done.html'

    class Meta:
        model = CustomUser


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'users/register.html'
  success_url = reverse_lazy('dashboard')
  form_class = CustomUserCreationForm
  success_message = "Account created"

# register -> singnup view
# success url -> login

def register(request):
    # zmienic na class based view
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
    print(request.user)
    login_details = LoginHistory.objects.filter(user=request.user).filter(login_result='False').aggregate(Max('login_time'))
    print(login_details)
    return render(request, 'users/dashboard.html', {'login_details': login_details})