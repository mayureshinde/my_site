from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=190)
    message = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.email
    

 