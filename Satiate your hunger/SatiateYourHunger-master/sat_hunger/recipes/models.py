from django.db import models
from users.models import *

# Create your models here.
class RecentSearches(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE,null=True)
    ingredients = models.CharField(max_length=1000)
    food_cat = models.CharField(max_length=20)
    hunger_level = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user.username}'s Search"

    class Meta: 
        verbose_name_plural = 'RecentSearches'