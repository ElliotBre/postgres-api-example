from django.db import models

# Create your models here.


class app(models.Model):
    name = models.CharField("Name", max_length=240)
