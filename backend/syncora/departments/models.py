from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Ensuring unique department names

    def __str__(self):
        return self.name