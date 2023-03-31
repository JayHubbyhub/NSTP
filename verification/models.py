from django.db import models
from django.core.validators import MaxValueValidator
import datetime

# Create your models here.
class Verification(models.Model):
    id_num = models.IntegerField(default=1, validators=[MaxValueValidator(9999999)])
    category = models.CharField(max_length=100, default="Umbrella")
    form = models.FileField(upload_to='files/')

    isChecked = models.BooleanField(default=False)

    submissionDate = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return'{}'.format(self.id)