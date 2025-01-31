from django.db import models

# Create your models here.

## Alamacenamiento de modelos persistentes
## Se defonen los modelos para almacenar datos

class DateItem(models.Model):
    color = models.CharField(max_length=50)
    fecha = models.DateField()
    model_id = models.CharField(max_length=100)
    watcher = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.color} - {self.fecha}"