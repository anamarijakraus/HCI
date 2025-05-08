from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Proizvoditel (models.Model):
    ime = models.CharField(max_length=50)
    lokacija = models.CharField(max_length=50)
    opis = models.CharField(max_length=200)
    datum_osnovanje = models.DateField()
    vo_eu = models.BooleanField()

    def __str__(self):
        return f"{self.ime}"


class MobilenUred (models.Model):
    TIP_CHOICES = [
        ("S", "Small"),
        ("M", "Medium "),
        ("L", "Large"),
    ]

    proizvoditel = models.ForeignKey(Proizvoditel, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    tip = models.CharField(max_length=1, choices=TIP_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    slika = models.ImageField(upload_to="phone_photos/", null=True, blank=True)
    cena =  models.IntegerField()
    godina_proizvodstvo = models.IntegerField()
    nov = models.BooleanField()