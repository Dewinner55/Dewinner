from django.urls import path
from .views import user_list, add_user, user_profile, edit_user, delete_user

urlpatterns = [
    path('users/', user_list, name='user_list'),
    path('add_user/', add_user, name='add_user'),
    path('user/<int:pk>/', user_profile, name='user_profile'),
    path('edit_user/<int:user_id>/', edit_user, name='edit_user'),
    path('users/<int:user_id>/edit/', edit_user, name='edit_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
]