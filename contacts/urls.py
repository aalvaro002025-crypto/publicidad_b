from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.create_contact, name='create_contact'),
    path('contacts/', views.list_contacts, name='list_contacts'),
    path('health/', views.health_check, name='health_check'),
]