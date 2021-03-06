from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('featured/', views.get_featured_posts, name='featured'),
    path('detailed/', views.get_content, name='detailed'),
    path('user-posts/', views.get_users_post, name='users-post'),
]