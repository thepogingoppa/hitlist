from django.db import models

# Create your models here.
class People(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name = models.CharField(max_length = 50)
    
    LOATHED = "L"
    IGNORED = "I"
    FORGIVEN = "F"

    STATUS_CHOICES = {
        LOATHED: "Loathed",
        IGNORED: "Ignored",
        FORGIVEN: "Forgiven",
    }

    status_choices = models.CharField(
        max_length=1, 
        choices=STATUS_CHOICES, 
        default=LOATHED
    )

    def __str__(self):
        return self.first_name + " " + self.last_name