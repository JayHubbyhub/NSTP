from django.urls import path
from django.conf.urls.static import static
from . import views   

urlpatterns = [
    path("treeRecords/", views.treeRecords.as_view(), name="treeRecords"),
    path("newTreeRecord/", views.newTreeRecord, name="newTreeRecord"),
    path('generate-qr/<str:data>/', views.generate_qr, name='generate_qr'),
]

app_name = "trees"