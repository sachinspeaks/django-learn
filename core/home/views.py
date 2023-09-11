from django.shortcuts import render
from django.http import HttpResponse
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




def home(request):
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