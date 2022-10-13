from django.urls import path
from todolist.views import show_todolist
from todolist.views import create_task
from todolist.views import register
from todolist.views import login_user
from todolist.views import logout_user
from todolist.views import delete_task
from todolist.views import delete_task_ajax
from todolist.views import status
from todolist.views import status_ajax
from todolist.views import show_todolist_ajax
from todolist.views import get_todolist_json
from todolist.views import show_json
from todolist.views import submit_ajax
app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('html/', show_todolist, name='show_todolist'),
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'),
    path('html/', show_todolist_ajax, name='show_todolist_ajax'),
    path('html/create-task/', create_task, name='create_task'),
    path('create-task/', create_task, name='create_task'),
    path('data-status/<int:id>', status, name='status'),
    path('html/data-status/<int:id>', status, name='status'),
    path('html/ajax/data-status/<int:id>', status, name='status'),
    path('ajax/data-status-ajax/<int:id>', status_ajax, name='status_ajax'),
    path('html/data-status-ajax/<int:id>', status_ajax, name='status_ajax'),
    path('delete-task/<int:id>', delete_task, name='delete_task'),
    path('html/delete-task/<int:id>', delete_task, name='delete_task'),
    path('html/ajax/delete-task-ajax/<int:id>', delete_task_ajax, name='delete_task_ajax'),
    path('ajax/delete-task-ajax/<int:id>', delete_task_ajax, name='delete_task_ajax'),
    path('html/ajax/delete-task/<int:id>', delete_task, name='delete_task'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('get-todolist-json/', get_todolist_json, name='get_todolist_json'),
    path('json/data-status/<int:id>', status, name='status'),
    path('json/delete/<int:id>', delete_task, name='delete'),
    path('json/', show_json, name='show_json'),
     path('/submit', submit_ajax, name="submit_ajax"),
]