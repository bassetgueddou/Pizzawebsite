from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# / menu


def index(request):
    ''' pizzas = Pizza.objects.all()
     pizzas_names = [pizza.nom + " : " +
                     str(pizza.prix) + " EURO " for pizza in pizzas]
     pizzas_names_str = ",".join(pizzas_names)
     return HttpResponse("Les pizzas : " + pizzas_names_str)'''
    pizzas = Pizza.objects.all()
    return render(request, 'menu/index.html', {'pizzas': pizzas})
