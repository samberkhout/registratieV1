from django.db import models


# Create your models here.
class Potting(models.Model):
    soort = models.CharField(max_length=100)
    leverweek = models.CharField(max_length=100)
    datum_van_check = models.DateField()
    aantal_opgepot = models.IntegerField()
    aantal_weggegooid = models.IntegerField()
    leverancier = models.CharField(max_length=100)
    werknemer = models.CharField(max_length=100)
    reden_weg_gooi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.soort} - {self.datum_van_check}"


class DiseaseSearch(models.Model):
    leverweek = models.IntegerField()
    oppot_week = models.IntegerField()
    leverancier = models.CharField(max_length=100)
    soort = models.CharField(max_length=100)
    hoeveel_geen_water = models.IntegerField()
    aantal_ziek_weggegooid = models.IntegerField()

    def __str__(self):
        return f"{self.soort} - Leverweek {self.leverweek}"


class TripsInfestationWeek10(models.Model):
    datum = models.DateField()
    oppot_week = models.IntegerField()
    lever_week = models.IntegerField()
    aantal_tafels = models.IntegerField()
    leverancier = models.CharField(max_length=100)
    soort = models.CharField(max_length=100)
    aantal_planten_weg_gooi = models.IntegerField()
    aantal_planten_schade = models.IntegerField()
    def __str__(self):
        return f"{self.soort} - Week {self.lever_week}"


class TripsInfestationWijdezetting(models.Model):
    datum = models.DateField()
    oppot_week = models.IntegerField()
    lever_week = models.IntegerField()
    aantal_tafels = models.IntegerField()
    leverancier = models.CharField(max_length=100)
    soort = models.CharField(max_length=100)
    aantal_planten_weg_gooi = models.IntegerField()
    aantal_planten_schade = models.IntegerField()

    def __str__(self):
        return f"{self.soort} - Week {self.lever_week} (Wijdezetting)"

