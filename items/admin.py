from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = ('description', 'locationFound', 'dateFound', 'timeFound')

admin.site.register(Item, ItemAdmin)