from django.shortcuts import render, redirect
from .models import Leadt
from .forms import LeadForm

# Create your views here.
def home_page(request):
    leads = Leadt.objects.all()
    context = {
        "leads":leads
    }
    return render(request, 'leads/leads_list.html', context)

def lead_detail(request, pk):
    lead = Leadt.objects.get(id=pk)
    context = {
        'lead':lead
    }

    return render(request, 'leads/lead_details.html', context)

def create_lead(request):
    form = LeadForm()
    if request.method == "POST":
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context ={
        'form':form
    }
    return render(request, 'leads/lead_create.html',context)
