from django.db import models

# Create your models here.
class Suplement (models.Model):
    KATEGORIJA_CHOICES = [
        ("p", "proteins"),
        ("v", "vitamins"),
        ("c", "creatines"),
        ("a", "amino acids"),
        ("w", "pre-workout ")
    ]
    ime = models.CharField(max_length=50)
    slika = models.ImageField(upload_to="suplement_photos/", null=True, blank=True)
    shifra = models.CharField(max_length=50)
    proizvoditel = models.CharField(max_length=50)
    dostapnost = models.BooleanField()
    kategorija = models.CharField(max_length=1, choices=KATEGORIJA_CHOICES)
    cena = models.IntegerField()

    def __str__(self):
        return f"{self.ime} {self.proizvoditel}"

