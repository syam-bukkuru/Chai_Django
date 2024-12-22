from django.shortcuts import render
from .models import chaiVerity

# Create your views here.
def all_chai(request):
    chais = chaiVerity.objects.all
    return render(request, 'chai/index.html',{'chais':chais})

