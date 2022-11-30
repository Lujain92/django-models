from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class Snack (models.Model):
    name = models.CharField(max_length=64, help_text="snack name", default="snack")
    #rank = models.IntegerField()
    desc= models.TextField(default="description")
    purchaser=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name