from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Menu(models.Model):
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    imgurl=models.CharField(max_length=255)
    vegORnonvegurl=models.CharField(max_length=255)
    
    def __str__(self):
        return self.name


class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(Menu, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.menu_item.name
    

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback = models.TextField()

    def __str__(self):
        return self.name

