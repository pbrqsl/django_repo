from django.urls import path
from . import views
from .views import ViewOne



urlpatterns = [
    path('fav_site/', views.fav_links),
    path('fav_links_render/', views.fav_links_render),
    path('fav_links_class/', ViewOne.as_view(), name='view-one')
]
