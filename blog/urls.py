from . import views
from django.urls import path

urlpatterns = [
    path('', views.Index, name='index'),
    # path('<str:user>/', views.user_page, name='user_page'),
    path('user_page/', views.user_page, name='user_page'),
    path('write_post/', views.write_post, name='write_post'),
    path('<slug:slug>/', views.view_full_post, name='view_full_post'),
    path('<slug:slug>/delete_post/<int:post_id>', views.delete_post, name='delete_post'),
]
