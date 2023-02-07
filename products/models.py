from django.db import models

#Aca aclaramos como queremos que se guarden los datos en la DB#
#Como creamos un producto??# creamos una clase
class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    stock = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True) #unique true es para que ninguna categoria se repita
    def __str__(self):
        return self.name