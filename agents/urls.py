from django.urls import path
from . import views
app_name = 'agents'

urlpatterns =[
    path('agent/',views.agent_list,name='agent'),
    path('create-agent/', views.create_agent, name='create-agent'),
    path('agent-details/<int:pk>/', views.agent_details, name='agent_details'),
]