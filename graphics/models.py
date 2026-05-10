from django.db import models
from django.utils.timezone import now


# Create your models here.
def fecha_actual():
    return now().date().strftime('%Y-%m-%d')

class History(models.Model):
      
      type_document = models.CharField(max_length=50)
      date = models.DateField(default= fecha_actual)

      def __str__(self):
           return self.type_document



