from django.contrib import admin
from .models import Verification

# Register your models here.
class VerificationAdmin(admin.ModelAdmin):
    model = Verification
    list_display = ("id_num", "category", "submissionDate", "form")

admin.site.register(Verification, VerificationAdmin)