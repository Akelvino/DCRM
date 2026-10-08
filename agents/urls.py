from django.urls import path
from . import views
app_name = 'agents'

urlpatterns =[
    path('agent/',views.agent_list,name='agent'),
    path('create-agent/', views.create_agent, name='create-agent'),
    path('agent-details/<int:pk>/', views.agent_details, name='agent_details'),
    path('edit_agent-details/<int:pk>/', views.edit_agent_details, name='edit_agent_details'),
    path('delete-agent/<int:pk>/', views.delete_agent, name='delete_agent')
]