from django.db import models

# Create your models here.
# class Branch(models.Model):
#     name=models.CharField(max_length=250)
#
#     def __str__(self):
#         return self.name

class Form(models.Model):
    name=models.CharField(max_length=250,default=True)
    dob=models.DateField(default=True)
    gender = models.TextField(default=True)
    number=models.IntegerField(default=True)
    email=models.EmailField(default=True)
    address=models.TextField(default=True)
    # district=models.CharField(max_length=250)
    # branches=models.TextField()
    # account=models.TextField()
    materialsprovided=models.TextField(default=True)


    def __str(self):
        return self.name


