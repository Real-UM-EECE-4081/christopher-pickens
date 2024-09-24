from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    complete = models.BooleanField(default=False)

    def __str__(self):
        return self.name