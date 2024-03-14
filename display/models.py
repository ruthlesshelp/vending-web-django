from django.db import models

# Create your models here.
class Coins(models.Model):
    quarters = models.IntegerField(blank=True, null=True)
    id = models.IntegerField(blank=True, primary_key=True)

    class Meta:
        managed = False
        db_table = 'coins'
