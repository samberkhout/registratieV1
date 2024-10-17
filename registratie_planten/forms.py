from registratie_planten.models import TripsInfestationWijdezetting, TripsInfestationWeek10, Potting, DiseaseSearch
from django import forms

class PottingForm(forms.ModelForm):
    class Meta:
        model = Potting
        fields = ['soort','lever_week', 'aantal_opgepot', 'aantal_weggegooid', 'werknemer', 'reden_weg_gooi']


class DiseaseSearchForm(forms.ModelForm):
    class Meta:
        model = DiseaseSearch
        fields = ['leverweek', 'oppot_week', 'soort', 'hoeveel_geen_water', 'aantal_ziek_weggegooid']


class TripsInfestationWeek10Form(forms.ModelForm):
    class Meta:
        model = TripsInfestationWeek10
        fields = ['oppot_week', 'lever_week', 'aantal_tafels', 'soort', 'aantal_planten_weg_gooi', 'aantal_planten_schade']


class TripsInfestationWijdezettingForm(forms.ModelForm):
    class Meta:
        model = TripsInfestationWijdezetting
        fields = ['oppot_week', 'lever_week', 'aantal_tafels', 'soort', 'aantal_planten_weg_gooi', 'aantal_planten_schade']
