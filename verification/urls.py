from django.urls import path
from . import views   

urlpatterns = [
    path('', views.verification, name='verification'),
    path('display/', views.displayVerForms, name='displayverforms'),
]

app_name = "verification"