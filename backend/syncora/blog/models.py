from django.db import models
from django.contrib.auth.models import User
from departments.models import Department

class Post(models.Model):
    autho = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title