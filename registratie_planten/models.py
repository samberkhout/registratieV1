from contextlib import nullcontext
from datetime import datetime, timezone
from django.utils import timezone
from django.db import models



class Leverancier(models.Model):
    naam = models.CharField(max_length=100)

    def __str__(self):
        return self.naam


class Soort(models.Model):
    naam = models.CharField(max_length=255, unique=True)
    leverancier = models.ForeignKey(Leverancier, on_delete=models.CASCADE)
    breeder_name = models.TextField(blank=True, null=True)
    var_kleur = models.TextField(blank=True, null=True)
    var_planthoogte = models.TextField(blank=True, null=True)
    var_bloemgrootte = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.naam


class PlantenInfoWeek(models.Model):
    name = models.ForeignKey(Soort, on_delete=models.CASCADE)
    week_nummer = models.IntegerField(default=1)
    var_bladlengte = models.TextField(blank=True, null=True)
    var_vertakkingen = models.TextField(blank=True, null=True)
    var_wortel = models.TextField(blank=True, null=True)
    var_1_spike = models.TextField(blank=True, null=True)
    var_2_spike = models.TextField(blank=True, null=True)
    var_3_spike = models.TextField(blank=True, null=True)
    var_potmaat = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ("name", "week_nummer")

    def __str__(self):
        return f"{self.name} - Week {self.week_nummer}"


class Potting(models.Model):
    soort = models.ForeignKey(Soort, on_delete=models.CASCADE)
    lever_week = models.IntegerField(null=True, blank=True)
    datum_van_check = models.DateField(default=timezone.now)
    aantal_opgepot = models.IntegerField()
    aantal_weggegooid = models.IntegerField()
    werknemer = models.CharField(max_length=100)
    reden_weg_gooi = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.soort} - {self.datum_van_check}"


class DiseaseSearch(models.Model):
    leverweek = models.IntegerField()
    soort = models.ForeignKey(Soort, on_delete=models.CASCADE)
    hoeveel_geen_water = models.IntegerField()
    aantal_ziek_weggegooid = models.IntegerField()

    def __str__(self):
        return f"{self.soort} - Leverweek {self.leverweek}"


class TripsInfestationWeek10(models.Model):
    datum = models.DateField(default=timezone.now)
    oppot_week = models.IntegerField()
    lever_week = models.IntegerField()
    aantal_tafels = models.IntegerField()
    soort = models.ForeignKey(Soort, on_delete=models.CASCADE)
    aantal_planten_weg_gooi = models.IntegerField()
    aantal_planten_schade = models.IntegerField()

    def __str__(self):
        return f"{self.soort} - Week {self.lever_week}"


class TripsInfestationWijdezetting(models.Model):
    datum = models.DateField(default=timezone.now)
    oppot_week = models.IntegerField()
    lever_week = models.IntegerField()
    aantal_tafels = models.IntegerField()
    soort = models.ForeignKey(Soort, on_delete=models.CASCADE)
    aantal_planten_weg_gooi = models.IntegerField()
    aantal_planten_schade = models.IntegerField()

    def __str__(self):
        return f"{self.soort} - Week {self.lever_week} (Wijdezetting)"


