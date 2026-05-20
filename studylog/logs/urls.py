from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_list, name='log_list'),
    
    path('create/',views.log_create,name='log_create'),
    
    path('update/<int:pk>/', views.log_update, name='log_update'),
    
    path('delete/<int:pk>/', views.log_delete, name='log_delete'),
]