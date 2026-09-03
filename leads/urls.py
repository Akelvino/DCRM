from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home'),
    path('details?/<int:pk>/', views.lead_detail, name='lead-detail'),
]