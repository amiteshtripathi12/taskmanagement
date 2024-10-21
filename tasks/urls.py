from django.urls import path
from .views import *

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/create/', CreateUserView.as_view(), name='create-user'),
    path('tasks/create/', create_new_task, name='create_new_task'),
    path('tasks/<int:task_id>/assign/', assign_users_to_task, name='assign_users_to_task'),
    path('users/<int:user_id>/tasks/', retrieve_user_tasks, name='retrieve_user_tasks'),
]
