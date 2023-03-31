from django.contrib import admin
from .models import Item
#from .models import Tree

#Register your models here.
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('description', 'locationFound', 'dateFound', 'timeFound')

# class ItemAdmin(admin.ModelAdmin):
#     model = Tree
#     list_display = ('section', 'age', 'variety', 'soil_moisture', 'temperature', 'humidity', 'light_exposure', 'nutrient_levels', 'pest_disease_outbreaks')

admin.site.register(Item, ItemAdmin)