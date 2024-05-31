from django.shortcuts import render
import datetime

# Create your views here.
def filters(request):
    da=datetime.datetime.now()
    d={'data':'Hai python How Are You','da':da,'c':10}
    return render(request,'filters.html',d)


def userfilters(request):
    d={'data':'hai Python How Are You'}
    return render(request,'userfilters.html',d)