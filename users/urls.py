
from django.urls import path
from .views import register, CustomLoginView, dashboard

urlpatterns = [
    path('register/', register),
    path('login/', CustomLoginView.as_view(template_name='users/login.html')),
    path('dashboard/', dashboard, name='dashboard')
]