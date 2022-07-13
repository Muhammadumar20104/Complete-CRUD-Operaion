from django.shortcuts import render
from django.http import HttpResponse
from . models import Details
from . forms import Df 
# Create your views here.
def Create(request):
    frm = Df
    if request.method == 'POST':
        frm= Df(request.POST)
        if frm.is_valid():
            frm.save()
            frm = Df()
    else:
        frm = Df()
    data = Details.objects.all()
    return render(request,"Form.html",{'Form':frm,'data':data})
def Read(request):
    var=Details.objects.all()
    return render(request,'Read.html',{'data':var})
def update(request,data):
    print(data)
    a=Details.objects.get(F_Name=data)
    va=Df(request.POST or None,instance=a)
    return  render(request,'Read.html',{'va':va})