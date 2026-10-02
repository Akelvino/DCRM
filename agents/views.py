from django.shortcuts import render
from leads.models import Agent

# Create your views here.
def agent_list(request):
    agents = Agent.objects.all()
    context = {"agents":agents}
    return render(request, 'agent/agent_list.html', context)