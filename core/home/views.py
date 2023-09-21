from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.conf import settings
from .models import *
import random
from .utils import send_email_to_client,send_email_with_attachment
# Create your views here.

peoples = [
    {"name": "Alice", "age": 10},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 15},
    {"name": "David", "age": 28},
    {"name": "Eve", "age": 22}
]

text="""Lorem ipsum, dolor sit amet consectetur adipisicing elit. Consequuntur quas doloribus aspernatur nemo iusto quod sequi, mollitia harum natus facere unde nisi illo repellat, asperiores, magni dolores modi qui. Commodi accusamus, possimus quam asperiores eum quo reprehenderit exercitationem aperiam iusto ea provident ipsam! Quae natus impedit rerum tempora architecto quasi ut quidem quod. Obcaecati, laboriosam error dicta officiis libero reiciendis harum praesentium dolorum laborum minima velit, asperiores eos vero commodi temporibus ipsa? Culpa dolores amet laboriosam itaque, nobis animi minus maiores atque repudiandae numquam quo nostrum, fugit cupiditate consequuntur ipsam. Dolores corporis vero fuga impedit, tempora asperiores incidunt soluta animi!"""

vegetables=['pumpkin','spinach','tomato']


def send_email(request):
    subject="This is a test Email from django server."
    message="Please find the attached file with this mail."
    recipient_list=['tempdjfgn@gmail.com']
    file_path=f"{settings.BASE_DIR}/mailattach.txt"
    # send_email_to_client()
    send_email_with_attachment(subject,message,recipient_list,file_path)
    return redirect('/')

car_names = [
    "Toyota Camry",
    "Honda Civic",
    "Ford Mustang",
    "Chevrolet Silverado",
    "Nissan Altima",
    "BMW 3 Series",
    "Mercedes-Benz C-Class",
    "Volkswagen Golf",
    "Tesla Model 3",
    "Jeep Wrangler",
]



def home(request):
    Car.objects.create(car_name=f"{car_names[random.randint(0,len(car_names))]} - model {random.randint(0,20)}")
    context={'page':'Django 2023 tutorial','peoples':peoples}
    return render(request,'./home/index.html',context)

def about(request):
    context={'page':'About'}
    return render(request,'./home/about.html',context)

def contact(request):
    context={'page':'Contact'}
    return render(request,'./home/contact.html',context)

def success_page(request):
    return HttpResponse("<h1>Hey this is a success Page.</h1>")