from django.db import models

# Create your models here.
class Item(models.Model):
    isLost = models.BooleanField(default=True)
    category = models.CharField(max_length=100, default="Umbrella")
    description = models.CharField(max_length=500)
    locationFound = models.CharField(max_length=100)
    dateFound = models.DateField()
    timeFound = models.TimeField(auto_now=False, auto_now_add=False)
    lost_item_image = models.ImageField(upload_to="lostItems", null=True, blank=True)

    
    def __str__(self):
        return'{}'.format(self.id)