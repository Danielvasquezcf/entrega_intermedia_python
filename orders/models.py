from django.db import models

class Order(models.Model):
    CHOICES = (
        ('Cash', 'Cash'),
        ('Card', 'Card'),
    )

    client = models.CharField(max_length=100)
    product = models.CharField(max_length=100)
    creation_time = models.DateTimeField(auto_now_add=True) #Este guarda la fecha hora minuto y segundo que se completa automaticamente y no es modificable#
    payment_method = models.CharField(choices=CHOICES, max_length=4)
    def __str__(self):
        return self.client, self.product
        
    
