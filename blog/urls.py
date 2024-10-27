from . import views
from django.urls import path

urlpatterns = [
    path('post/<slug:slug>/', views.view_full_post, name='view_full_post'),
    path('write_post/', views.write_post, name='write_post'),
    path('<slug:slug>/delete_post/<int:post_id>', views.delete_post, name='delete_post'),
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('', views.Index, name='index'),
]
