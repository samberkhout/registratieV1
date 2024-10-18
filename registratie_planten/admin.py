from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Soort, Leverancier, Potting, DiseaseSearch, TripsInfestationWeek10, TripsInfestationWijdezetting

# Register your models here.
@admin.register(Leverancier)
class LeverancierAdmin(admin.ModelAdmin):
    list_display = ('naam',)
    search_fields = ('naam',)

@admin.register(Soort)
class SoortAdmin(admin.ModelAdmin):
    list_display = ('naam', 'leverancier', 'breeder_name', 'var_kleur', 'var_planthoogte', 'var_bloemgrootte')
    search_fields = ('naam', 'leverancier__naam')
    list_filter = ('leverancier',)

@admin.register(Potting)
class PottingAdmin(admin.ModelAdmin):
    list_display = ('soort', 'lever_week', 'datum_van_check', 'aantal_opgepot', 'aantal_weggegooid', 'werknemer', 'reden_weg_gooi')
    search_fields = ('soort__naam', 'werknemer')
    list_filter = ('datum_van_check', 'soort')

@admin.register(DiseaseSearch)
class DiseaseSearchAdmin(admin.ModelAdmin):
    list_display = ('soort', 'leverweek', 'hoeveel_geen_water', 'aantal_ziek_weggegooid')
    search_fields = ('soort__naam',)
    list_filter = ('leverweek','soort')

@admin.register(TripsInfestationWeek10)
class TripsInfestationWeek10Admin(admin.ModelAdmin):
    list_display = ('soort', 'lever_week', 'oppot_week', 'datum', 'aantal_tafels', 'aantal_planten_weg_gooi', 'aantal_planten_schade')
    search_fields = ('soort__naam',)
    list_filter = ('datum', 'lever_week', 'oppot_week')

@admin.register(TripsInfestationWijdezetting)
class TripsInfestationWijdezettingAdmin(admin.ModelAdmin):
    list_display = ('soort', 'lever_week', 'oppot_week', 'datum', 'aantal_tafels', 'aantal_planten_weg_gooi', 'aantal_planten_schade')
    search_fields = ('soort__naam',)
    list_filter = ('datum', 'lever_week', 'oppot_week')