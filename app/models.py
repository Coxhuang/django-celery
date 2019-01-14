from django.db import models

class CeleryModels(models.Model):

    time = models.DateTimeField(auto_now_add=True)
