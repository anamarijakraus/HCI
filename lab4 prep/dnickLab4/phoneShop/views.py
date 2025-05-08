from django.shortcuts import render

from phoneShop.models import MobilenUred


# Create your views here.
def index(request):
    phones_list = MobilenUred.objects.all()
    context = {'phones_list': phones_list}
    return render(request, 'index.html', context)


def details(request, phone_id):
    phone = MobilenUred.objects.filter(id=phone_id).first()
    context = {'phone': phone}
    return render(request, 'details.html', context)
