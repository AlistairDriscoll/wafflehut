from . import views
from django.urls import path
from django.contrib.auth.models import User

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
]
