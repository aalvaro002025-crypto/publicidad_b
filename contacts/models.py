from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField()
    phone = models.CharField(max_length=25)
    country = models.CharField(max_length=20)
    company = models.CharField(max_length=100, blank=True, null=True)  # Nueva campo
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.country} - {self.company or 'Sin empresa'}"
