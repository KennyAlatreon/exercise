from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user_in', views.user_in, name='user_in'),
    path('user_out', views.user_out, name='user_out'),
    path('message', views.message, name='message'),
]
