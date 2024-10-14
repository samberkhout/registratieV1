from django.shortcuts import render, redirect
from django.views import View
from .forms import PottingForm, DiseaseSearchForm, TripsInfestationWijdezettingForm, TripsInfestationWeek10Form


# Views
class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')


class PottingView(View):
    def get(self, request):
        form = PottingForm()
        return render(request, 'potting_form.html', {'form': form})

    def post(self, request):
        form = PottingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'potting_form.html', {'form': form})


class DiseaseSearchView(View):
    def get(self, request):
        form = DiseaseSearchForm()
        return render(request, 'disease_search_form.html', {'form': form})

    def post(self, request):
        form = DiseaseSearchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'disease_search_form.html', {'form': form})


class TripsInfestationWeek10View(View):
    def get(self, request):
        form = TripsInfestationWeek10Form()
        return render(request, 'trips_infestation_week10_form.html', {'form': form})

    def post(self, request):
        form = TripsInfestationWeek10Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'trips_infestation_week10_form.html', {'form': form})


class TripsInfestationWijdezettingView(View):
    def get(self, request):
        form = TripsInfestationWijdezettingForm()
        return render(request, 'trips_infestation_wijdezetting_form.html', {'form': form})

    def post(self, request):
        form = TripsInfestationWijdezettingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        return render(request, 'trips_infestation_wijdezetting_form.html', {'form': form})
