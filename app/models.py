from django.db import models

class CeleryModels(models.Model):

    time = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=128,default="")
