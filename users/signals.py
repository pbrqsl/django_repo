from .models import CustomUser
from django.db.models.signals import post_save
from django.contrib.auth.signals import user_login_failed, user_logged_in
from django.dispatch import receiver
from .models import UserProfile, LoginHistory


@receiver(post_save, sender=CustomUser)
def CreateProfile(sender, instance, created, **kwargs):
    if created:
        print('create_profile')
        print(instance.date_joined)
        UserProfile.objects.create(user=instance)

# @receiver(post_save, sender=CustomUser)
# def save_profile(sender, instance, **kwargs):
#     print('save_profile')
#     instance.profile.save(user=instance)

@receiver(user_logged_in, sender=CustomUser)
def log_success_login(sender, user, **kwargs):
    #print('wooooo')
    print(user)
    LoginHistory.objects.create(user=user, login_result=True)

@receiver(user_login_failed)
def log_failed_login(sender, credentials, **kwargs):
    #print('wooooo')
    print(credentials)
    try:
        user = CustomUser.objects.get(email=credentials['username'])
    except:
        user = None
    print(user)
    LoginHistory.objects.create(user=user, login_result=False)
    

    #zrobic na foreign key
