from django.shortcuts import render
from django.shortcuts import render
from django.shortcuts import render
from lab.models import Users
from lab.models import Recipes
from lab.models import Products
from lab.models import Composition


def home(request):
 return render(request, 'base.html', {'data': {
  'Recipes': Recipes.objects.all(),
  'Users': Users.objects.all()
 }})

def recipe(request, id):

    return render(request, 'recipes_info.html', {'data': {
        'Recipe': Recipes.objects.filter(id=id)[0],
    }})
def user(request, id):

    return render(request, 'Users_info.html', {'data': {
        'Users': Users.objects.filter(id=id)[0],
        'Recipes': Recipes.objects.filter(Users_id=id)
    }})

# Create your views here
