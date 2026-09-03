from django.shortcuts import render
from .models import Leadt
# Create your views here.
def home_page(request):
    leads = Leadt.objects.all()
    context = {
        "leads":leads
    }
    return render(request, 'leads/leads_list.html', context)