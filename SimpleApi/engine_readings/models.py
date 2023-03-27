from django.db import models

# Create your models here.

class Engine(models.Model):
    objects = models.Manager
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'Motor: ({self.name})'

class Reading(models.Model):
    objects = models.Manager()
    value = models.IntegerField()
    engine = models.ForeignKey(Engine, on_delete= models.CASCADE)

    def __str__(self):
        return f'{self.engine}: {self.pk}-{self.value}'

