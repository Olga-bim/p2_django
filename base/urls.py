from django.http import HttpResponse
from django.urls import path

from base import admin
from . import views

# Определяем простую главную страницу
def home(request):
    return HttpResponse("Welcome to the Home Page")

urlpatterns = [
    
    path('', home, name='home'),  # Маршрут для главной страницы
   
    # URL для списка животных и создания нового животного
    path('animals/', views.animals_list, name='animals-list'),

    # URL для получения информации о животном
    path('animals/<int:pk>/', views.animal_detail_get, name='animal-detail-get'),

    # URL для обновления информации о животном
    path('animals/<int:pk>/update/', views.animal_detail_put, name='animal-detail-put'),

    # URL для удаления животного
    path('animals/<int:pk>/delete/', views.animal_detail_delete, name='animal-detail-delete'),

    # URL для списка клиентов и создания нового клиента
    path('clients/', views.clients_list, name='clients-list'),

    # URL для получения информации о клиенте
    path('clients/<int:pk>/', views.client_detail_get, name='client-detail-get'),

    # URL для обновления информации о клиенте
    path('clients/<int:pk>/update/', views.client_detail_put, name='client-detail-put'),

    # URL для удаления клиента
    path('clients/<int:pk>/delete/', views.client_detail_delete, name='client-detail-delete'),

    # URL для списка студентов и создания нового студента
    path('students/', views.students_list, name='students-list'),

    # URL для получения информации о студенте
    path('students/<int:pk>/', views.students_detail_get, name='students-detail-get'),

    # URL для обновления информации о студенте
    path('students/<int:pk>/update/', views.students_detail_put, name='students-detail-put'),

    # URL для удаления студента
    path('students/<int:pk>/delete/', views.students_detail_delete, name='students-detail-delete'),
]