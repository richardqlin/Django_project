from django.db import models


class OneStopShop(models.Model):
    title = models.CharField(max_length=20,unique=True)
    description = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    unit = models.CharField(max_length=10)
    quantity = models.IntegerField()
    image = models.CharField(max_length=200)

    def __str__(self):
        return '%s %s %s %s %d %s' %(self.title, self.description, self.price, self.unit, self.quantity, self.image)



# Create your models here.
