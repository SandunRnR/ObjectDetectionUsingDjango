from django.db import models

# Create your models here.

class Object(models.Model):
    class_name = models.CharField(max_length=200)
    confidence = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.name