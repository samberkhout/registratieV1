from django import forms
from .models import Potting, DiseaseSearch, TripsInfestationWeek10, TripsInfestationWijdezetting


class PottingForm(forms.ModelForm):
    class Meta:
        model = Potting
        fields = ['soort', 'datum_van_check', 'aantal_opgepot', 'aantal_weggegooid', 'leverancier', 'werknemer', 'reden_weg_gooi']


class DiseaseSearchForm(forms.ModelForm):
    class Meta:
        model = DiseaseSearch
        fields = ['leverweek', 'oppot_week', 'leverancier', 'soort', 'hoeveel_geen_water', 'aantal_ziek_weggegooid']


class TripsInfestationWeek10Form(forms.ModelForm):
    class Meta:
        model = TripsInfestationWeek10
        fields = ['datum', 'oppot_week', 'lever_week', 'aantal_tafels', 'leverancier', 'soort', 'aantal_planten_weg_gooi', 'aantal_planten_schade']


class TripsInfestationWijdezettingForm(forms.ModelForm):
    class Meta:
        model = TripsInfestationWijdezetting
        fields = ['datum', 'oppot_week', 'lever_week', 'aantal_tafels', 'leverancier', 'soort', 'aantal_planten_weg_gooi', 'aantal_planten_schade']

