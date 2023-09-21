from django.db import models
from django.db.models.signals import post_save,post_delete,pre_delete,pre_save
from django.dispatch import receiver
# Create your models here.

class Student(models.Model):
    name=models.CharField(default="Sachin",max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    address=models.TextField(null=True,blank=True)
    file=models.FileField()

class Car(models.Model):
    car_name=models.CharField(max_length=100)
    speed=models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name
    
@receiver(post_save,sender=Car)
def call_car_api(sender,instance,**kwargs):
    print("car object created.")
    print(sender,instance,kwargs)