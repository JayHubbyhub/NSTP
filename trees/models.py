from django.db import models

# Create your models here.
class Tree(models.Model):
    section = models.CharField(max_length=100, default="Tree")
    age = models.CharField(max_length=500)
    variety = models.CharField(max_length=500)
    soil_moisture = models.CharField(max_length=500)
    temperature = models.CharField(max_length=500)
    humidity = models.CharField(max_length=500)
    light_exposure = models.CharField(max_length=500)
    nutrient_levels = models.CharField(max_length=500)
    pest_disease_outbreaks = models.CharField(max_length=500)
    harvestTime = models.TimeField(auto_now=False, auto_now_add=False)
    harvestDate = models.DateField(null=True, blank=True)
    tree_image = models.ImageField(upload_to="treeRecords", null=True, blank=True)

    
    def __str__(self):
        return'{}'.format(self.id)