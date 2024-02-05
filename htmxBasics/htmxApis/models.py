from django.db import models

# Create your models here.
class Personnel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        db_table = "personnel"
        ordering = ['age']