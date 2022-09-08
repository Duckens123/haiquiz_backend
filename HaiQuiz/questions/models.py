from django.db import models

# Create your models here.
class Question(models.Model):
    libelle=models.CharField(max_length=255, blank=False)
    ops1=models.CharField(max_length=255, blank=False)
    ops2=models.CharField(max_length=255, blank=False)
    ops3=models.CharField(max_length=255, blank=False)
    ops4=models.CharField(max_length=255, blank=True)
    ans=models.CharField(max_length=255, blank=False)

    def __str__(self):
        return self.libelle
