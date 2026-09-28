from django.shortcuts import render, redirect, get_object_or_404
from .models import Leadt
from .forms import LeadForm, CreateUserForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home_page(request):
    leads = Leadt.objects.all()
    context = {
        "leads":leads
    }
    return render(request, 'leads/leads_list.html', context)

@login_required
def lead_detail(request, pk):
    lead = Leadt.objects.get(id=pk)
    context = {
        'lead':lead
    }

    return render(request, 'leads/lead_details.html', context)

@login_required
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

@login_required
def edit_lead(request,pk):
    lead = get_object_or_404(Leadt, id=pk)
    
    if request.method == 'POST':
        form = LeadForm(request.POST,instance=lead)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = LeadForm(instance = lead)
    context ={
        "form":form,
        "lead" : lead
    }
    return render(request, 'leads/edit_lead.html', context)

@login_required
def delete_lead(request,pk):
    lead = get_object_or_404(Leadt, id=pk)
    lead.delete()
    return redirect('home')


def signup(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context ={
      'form':form,  
    }
    return render(request, 'registration/signup.html',context)