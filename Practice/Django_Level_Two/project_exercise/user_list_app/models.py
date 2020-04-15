from django.db import models

# Create your models here.

class Users(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    email = models.URLField(unique = True, max_length = 200)

    def __str__(self):
        return self.first_name