from django.db import models

# Create your models here.


class Todo(models.Model):
    item = models.CharField(max_length=50, blank=False, default=None)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
