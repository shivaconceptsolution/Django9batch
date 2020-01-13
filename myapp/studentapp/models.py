from django.db import models

# Create your models here.
class Register(models.Model):
 emailid= models.CharField(max_length=50)
 password= models.CharField(max_length=10)
 mobile= models.CharField(max_length=10)
 fullname= models.CharField(max_length=40)
 address=models.CharField(max_length=40)
 def __str__(self):
   return "emailid is "+str(self.emailid)+" password is "+self.password+" mobile no is"+self.mobile+" fullname is "+self.fullname+" address is "+self.address 