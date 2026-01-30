from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.main_view, name='main_view'),
    path('tasklist/', views.task_list, name='task_list'),
    path('tasklist/create/', views.create_task, name="create_task"),
    path('tasklist/delete/<int:task_id>', views.delete_task, name="delete_task"),
    path('tasklist/update/<int:task_id>', views.update, name="update_task"),

    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

#    path('login/', views.login, name='login'),
#    path('register/', views.register, name='register'),lolkek