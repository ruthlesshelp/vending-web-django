from django.db import models

# Create your models here.
class Cache(models.Model):
    quarters = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, primary_key=True)
