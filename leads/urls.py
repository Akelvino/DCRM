from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('details?/<int:pk>/', views.lead_detail, name='lead-detail'),
    path('update/<int:pk>/', views.edit_lead, name='lead-update'),
    path('delete/<int:pk>/', views.delete_lead, name='lead-delete'),
    path('create/', views.create_lead, name='create-lead'),
]