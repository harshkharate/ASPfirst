from django.shortcuts import render
from .forms import RequestForm
from django.http import HttpResponse
from .models import Request


# Create your views here.
def hi(request):
    form = RequestForm(request.POST or None)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render (request, "REQUESTAPP/home.html",context)
