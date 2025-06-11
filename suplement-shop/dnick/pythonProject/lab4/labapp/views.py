from django.shortcuts import render
from labapp.models import Suplement
# Create your views here.
def index(request):
    suplement_list = Suplement.objects.all()
    context = {'suplement_list': suplement_list}
    return render(request, 'index.html', context)


def details(request, suplement_id):
    suplement = Suplement.objects.filter(id=suplement_id).first()
    context = {'suplement': suplement}
    return render(request, 'details.html', context)