from cityapp.forms import PopulationRegistration
from django.shortcuts import render, HttpResponseRedirect
from .models import Population
from django.contrib.auth.models import UserManager
from django.core.paginator import Paginator

# Create your views here.

def population_show(request):
    if request.method == "POST":
        fm = PopulationRegistration(request.POST)
        if fm.is_valid():
            fm.save()
        fm = PopulationRegistration()
    else:
        fm = PopulationRegistration()
    form = Population.objects.all()
    paginator = Paginator(form,15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, "cityapp/index.html", {"forms" : page_obj , "fm": fm})

def update_data(request,id):
    if request.method == "POST":
        pi = Population.objects.get(pk=id)
        fm = PopulationRegistration(instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = Population.objects.get(pk=id)
        fm = PopulationRegistration(instance=pi)
    return render(request, 'cityapp/updatecity.html', {"forms":fm})

def delete_data(request, id):
    if request.method == 'POST':
        pi = Population.objects.get(pk=id)
        pi.delete()
    return HttpResponseRedirect('/')