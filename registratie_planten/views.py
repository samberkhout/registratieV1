from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse
from .forms import PottingForm, DiseaseSearchForm, TripsInfestationWijdezettingForm, TripsInfestationWeek10Form
from .models import Soort

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
            potting = form.save(commit=False)
            soort_id = request.POST.get('soort')
            if soort_id:
                potting.soort = Soort.objects.get(id=soort_id)
            potting.save()
            return redirect('home')
        return render(request, 'potting_form.html', {'form': form})


class DiseaseSearchView(View):
    def get(self, request):
        form = DiseaseSearchForm()
        return render(request, 'disease_search_form.html', {'form': form})

    def post(self, request):
        form = DiseaseSearchForm(request.POST)
        if form.is_valid():
            disease_search = form.save(commit=False)
            soort_id = request.POST.get('soort')
            if soort_id:
                disease_search.soort = Soort.objects.get(id=soort_id)
            disease_search.save()
            return redirect('home')
        return render(request, 'disease_search_form.html', {'form': form})


class TripsInfestationWeek10View(View):
    def get(self, request):
        form = TripsInfestationWeek10Form()
        return render(request, 'trips_infestation_week10_form.html', {'form': form})

    def post(self, request):
        form = TripsInfestationWeek10Form(request.POST)
        if form.is_valid():
            trips_infestation = form.save(commit=False)
            soort_id = request.POST.get('soort')
            if soort_id:
                trips_infestation.soort = Soort.objects.get(id=soort_id)
            trips_infestation.save()
            return redirect('home')
        return render(request, 'trips_infestation_week10_form.html', {'form': form})


class TripsInfestationWijdezettingView(View):
    def get(self, request):
        form = TripsInfestationWijdezettingForm()
        return render(request, 'trips_infestation_wijdezetting_form.html', {'form': form})

    def post(self, request):
        form = TripsInfestationWijdezettingForm(request.POST)
        if form.is_valid():
            trips_infestation = form.save(commit=False)
            soort_id = request.POST.get('soort')
            if soort_id:
                trips_infestation.soort = Soort.objects.get(id=soort_id)
            trips_infestation.save()
            return redirect('home')
        return render(request, 'trips_infestation_wijdezetting_form.html', {'form': form})


def search_soorten(request):
    query = request.GET.get('query', '')
    if query:
        results = Soort.objects.filter(naam__icontains=query)
        return JsonResponse({'results': [{'id': soort.id, 'name': soort.naam} for soort in results]})
    return JsonResponse({'results': []})
