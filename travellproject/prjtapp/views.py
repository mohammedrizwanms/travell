from django.http import HttpResponse
from django.shortcuts import render
from . models import prjttable
from .models import team

# Create your views here.
def demo(request):

    obj=prjttable.objects.all()
    obj1=team.objects.all()

    return render(request, "index.html", {'result':obj,'res':obj1})
