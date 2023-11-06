
from django.urls import path
from .views import register, CustomLoginView, dashboard, SignUpView, CustomPasswordReset, CustomPasswordResetDone

urlpatterns = [
    #path('register/', register),
    path('register/', SignUpView.as_view()),
    path('login/', CustomLoginView.as_view(template_name='users/login.html')),
    path('dashboard/', dashboard, name='dashboard'),
    path('reset_password/', CustomPasswordReset.as_view(), name='password_reset'),
    path('reset_password_done/', CustomPasswordResetDone.as_view(), name='password_reset_done'),
]