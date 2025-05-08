from django.db import models

# Create your models here.
class Note(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    status = models.TextField(max_length=20)
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name