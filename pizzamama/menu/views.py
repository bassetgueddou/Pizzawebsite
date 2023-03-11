from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# / menu


def index(request):
    pizzas = Pizza.objetcts.all()
    pizzas_names = [pizza.nom for pizza in pizzas]
    pizzas_names_str = ", ".join(pizzas_names)
    return HttpResponse("Les pizzas : " + pizzas_names_str)
