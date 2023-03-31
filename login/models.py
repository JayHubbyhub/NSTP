from django.db import models
from django.core.validators import MaxValueValidator

DEFAULT_ID_NUM = 1

# Create your models here.
class User(models.Model):
    id_num = models.IntegerField(default=DEFAULT_ID_NUM, validators=[MaxValueValidator(9999999)], primary_key=True)
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    password = models.CharField(max_length=16)
    administrator = models.BooleanField(default=False)

    def __str__(self):
        if (self.administrator):
            return 'Admin: {} {}'.format(self.first_name, self.last_name)

        return 'Student: {} {}'.format(self.first_name, self.last_name)