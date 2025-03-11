from django.urls import path
from . import views

urlpatterns = [
    path('category/list', views.categoryList, name='category_list'),

    path('category/create', views.categoryCreate, name='category_create'),
    path('category/store', views.categoryStore, name='category_store'),


    path('category/edit/<pk>', views.categoryEdit, name='category_edit'),
    path('category/update/<pk>', views.categoryUpdate, name='category_update'),
    path('category/delete/<pk>', views.categoryDelete, name='category_delete'),




    path('todo/list', views.todoList, name='todo_list'),

    path('todo/create', views.todoCreate, name='todo_create'),
    path('todo/store', views.todoStore, name='todo_store'),


    path('todo/edit/<pk>', views.todoEdit, name='todo_edit'),
    path('todo/update/<pk>', views.todoUpdate, name='todo_update'),
    path('todo/delete/<pk>', views.todoDelete, name='todo_delete'),
    path('todo/complate/<pk>', views.todoComplete, name='todo_complete'),
]

