from django.contrib import admin
from .models import Pizza


class PizzaAdmin(admin.ModelAdmin):
    list_display = ('nom', 'Ingredients', 'prix', 'vegetarienne')
    search_fields = ('nom', 'Ingredients')


admin.site.register(Pizza, PizzaAdmin)
