from . import views
from django.urls import path
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    # path('<str:user>/', views.user_page, name='user_page'),
    path('user_page/', views.user_page, name='user_page'),
]
