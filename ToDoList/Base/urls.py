from django.urls import path
from . import views

urlpatterns = [
    path('', views.tasks, name='base'),
    path('edit_task/<int:id>', views.edit_task, name='edit_task'),
    path('remove/<int:id>', views.remove_task, name='remove_task'),
    path('new_task/', views.new_task, name='new_task'),
    path('search/', views.search, name='search'),
    path('login/', views.Authenticate.as_view(), name='login'),
    path('register/', views.Register.as_view(), name='register'),
    path('logout/', views.close_session, name='logout'),
]