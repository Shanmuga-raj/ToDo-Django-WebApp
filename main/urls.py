from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),

    path('add/', views.addTodo, name='add'),
    path('completed/<todo_id>/', views.completeTodo, name='complete'),
    path('deletecomplete/', views.deleteCompleted, name='deletecompleted'),
    path('deleteall/', views.deleteAll, name='deleteall')
]
