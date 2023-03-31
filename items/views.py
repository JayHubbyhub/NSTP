from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from .models import Item
from .forms import ItemForm
from django.template.loader import get_template
from django.views import View


# Create your views here.
class lostItems(View):
    template = "lostitems.html"
    def get(self, request):
        all_lost_items = Item.objects.filter(isLost=True)
        context = {
            "all_lost_items": all_lost_items
        }
        
        return render(request, "items/lostitems.html", context)
    
def newLostItem(request):
    if request.method == "POST":
        lost_item_form = ItemForm(request.POST, request.FILES)
        if lost_item_form.is_valid():
            lost_item_form.save()
            return redirect("items:newLostItem")
        else:
            lost_item_form = ItemForm()
    return render(request, "items/add.html", {"lost_item_form": ItemForm})
