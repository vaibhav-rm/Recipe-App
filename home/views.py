from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

@login_required(login_url="/login/")
def index(request):
    if request.method == "POST":
         
        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
         
        Recipe.objects.create(
                recipe_image = recipe_image,
                recipe_name = recipe_name,
                recipe_description = recipe_description
                )
        return redirect('/')
    queryset = Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id = id)
    queryset.delete()
    return redirect("/")

@login_required(login_url="/login/")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id = id)

    if request.method == "POST":

        data = request.POST
        recipe_image = request.FILES.get('recipe_image')
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect('/')
    context = {'recipe': queryset}
    return render(request, 'home/update_recipes.html', context)

def login_page(request):

    if request.method =="POST":
        
        data = request.POST
        username = data.get('username')
        password = data.get('password')

        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.warning(request, "Invalid Credentials")
            return redirect('/login/')

    return render(request, "home/login.html")

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    
    if request.method == "POST":
        
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        
        if User.objects.filter(username = username).exists():
            messages.warning(request, "Username already taken")
            return redirect('/register/')

        user = User.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                username = username
                )
        
        user.set_password(password)
        user.save()
        messages.success(request, "Account Created Scucessfully")

    return render(request, "home/register.html")
