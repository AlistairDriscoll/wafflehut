from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name='index'),
    # path('<str:user>/', views.user_page, name='user_page'),
    path('user_page/', views.user_page, name='user_page'),
    path('write_post/', views.write_post, name='write_post'),
]
