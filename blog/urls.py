from . import views
from django.urls import path

urlpatterns = [
    path('delete_account/', views.delete_account, name='delete_account'),
    path('post/<slug:slug>/', views.view_full_post, name='view_full_post'),
    path('write_post/', views.write_post, name='write_post'),
    path('edit_user/<str:username>/', views.edit_user, name="edit_user"),
    path(
        'post/<slug:slug>/delete_post/',
        views.delete_post,
        name='delete_post'
        ),
    path(
        'post/<slug:slug>/edit_post/<int:post_id>/',
        views.edit_post, name='edit_post'
        ),
    path('user/<str:username>/', views.user_page, name='user_page'),
    path('', views.index, name='index'),
]
