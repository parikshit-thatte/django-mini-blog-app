from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('blogs/', views.view_all_blogs, name='view_all_blogs'),
    path('bloggers/', views.view_all_authors, name='view_all_authors'),
    path('blogs/<int:blog_id>/', views.view_blog, name='view_blog'),
    path('bloggers/<int:blogger_id>', views.view_author, name='view_author'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]