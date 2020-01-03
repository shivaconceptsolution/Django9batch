from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request,"siapp/silogic.html")
def silogic(request):
	p=request.GET["txtnum1"]
	r=request.GET["txtnum2"]
	t=request.GET["txtnum3"]
	si=(float(p)*float(r)*float(t))/100
	return HttpResponse("result is "+str(si))

