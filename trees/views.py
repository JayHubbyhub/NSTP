from django.shortcuts import render, redirect
from django.template import Template, Context, loader
from .models import Tree
from .forms import TreeRecordForm
from django.template.loader import get_template
from django.views import View


# Create your views here.
class treeRecords(View):
    template = "treeRecords.html"
    def get(self, request):
        all_tree_records = Tree.objects.filter()
        context = {
            "all_tree_records": all_tree_records
        }
        
        return render(request, "trees/treeRecords.html", context)
    
def newTreeRecord(request):
    if request.method == "POST":
        tree_record_form = TreeRecordForm(request.POST, request.FILES)
        if tree_record_form.is_valid():
            tree_record_form.save()
            return redirect("trees:newTreeRecord")
        else:
            tree_record_form = TreeRecordForm()
    return render(request, "trees/add.html", {"tree_record_form": TreeRecordForm})
