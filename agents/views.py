from django.shortcuts import render, redirect
from leads.models import Agent
from django.contrib.auth.decorators import login_required
from .forms import AgentModelForm


# Create your views here.
@login_required
def agent_list(request):
    agents = Agent.objects.all()
    context = {"agents":agents}
    return render(request, 'agent/agent_list.html', context)


@login_required
def create_agent(request):
    form = AgentModelForm()
    if request.method == 'POST':
        form = AgentModelForm(request.POST)
        if form.is_valid():
            agent = form.save(commit=False)
            agent.organisation = request.user.userprofile
            agent.save()
            return redirect("agents:agent")
    context = {'form':form}
    return render(request,'agent/agent_create.html', context)