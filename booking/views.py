from django.shortcuts import render

# Create your views here.


def home_page(request):
    return render(request, 'booking/index.html')


def open_contacts(request):
    return render(request, 'booking/contacts.html')
