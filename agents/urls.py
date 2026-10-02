from django.urls import path
from . import views
app_name = 'agents'

urlpatterns =[
    path('agent/',views.agent_list,name='agent')
]