from django.shortcuts import render
from django.http import HttpResponse
from .models import Register
def index(request):
	return render(request,"studentapp/index.html")
def indexlogic(request):
     email = request.POST["txtemail"]
     pass1 = request.POST["txtpass"]
     mobile = request.POST["txtmobile"]
     fname = request.POST["txtfullname"]
     address = request.POST["txtaddress"]
     s = Register(emailid=email,password=pass1,mobile=mobile,fullname=fname,address=address)
     s.save()
     return render(request,"studentapp/index.html",{'res':'registration successfully'})
