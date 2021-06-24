from django.db import models

# Create your models here.


class item(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    kwh = models.FloatField(verbose_name='kWh')
    image = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.name
