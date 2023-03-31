from django.urls import path
from . import views   

urlpatterns = [
    path('', views.verification, name='verification'),
    path('display/', views.displayVerForms, name='displayverforms'),
    path('generate-qr/<str:data>/', views.generate_qr, name='generate_qr'),
]

app_name = "verification"