from django.shortcuts import render
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
                try:
                    potting.soort = Soort.objects.get(id=soort_id)
                except Soort.DoesNotExist:
                    return JsonResponse({'error': 'Ongeldige soort geselecteerd.'}, status=400)
            else:
                return JsonResponse({'error': 'Soort is vereist.'}, status=400)
            potting.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Formuliergegevens zijn ongeldig.'}, status=400)


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
                try:
                    disease_search.soort = Soort.objects.get(id=soort_id)
                except Soort.DoesNotExist:
                    return JsonResponse({'error': 'Ongeldige soort geselecteerd.'}, status=400)
            else:
                return JsonResponse({'error': 'Soort is vereist.'}, status=400)
            disease_search.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Formuliergegevens zijn ongeldig.'}, status=400)


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
                try:
                    trips_infestation.soort = Soort.objects.get(id=soort_id)
                except Soort.DoesNotExist:
                    return JsonResponse({'error': 'Ongeldige soort geselecteerd.'}, status=400)
            else:
                return JsonResponse({'error': 'Soort is vereist.'}, status=400)
            trips_infestation.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Formuliergegevens zijn ongeldig.'}, status=400)


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
                try:
                    trips_infestation.soort = Soort.objects.get(id=soort_id)
                except Soort.DoesNotExist:
                    return JsonResponse({'error': 'Ongeldige soort geselecteerd.'}, status=400)
            else:
                return JsonResponse({'error': 'Soort is vereist.'}, status=400)
            trips_infestation.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'error': 'Formuliergegevens zijn ongeldig.'}, status=400)


class HormoonSpuitView(View):
    def get(self, request):
        return render(request, 'hormoon_spuit_per_soort.html')


def search_soorten(request):
    query = request.GET.get('query', '')
    if query:
        results = Soort.objects.filter(naam__icontains=query)
        return JsonResponse({'results': [{'id': soort.id, 'name': soort.naam} for soort in results]})
    return JsonResponse({'results': []})


def get_hormoon_spuit(request):
    soort_id = request.GET.get('soort_id')
    try:
        soort = Soort.objects.get(id=soort_id)
        return JsonResponse({'hormoon_spuit': soort.hormoon_spuit})
    except Soort.DoesNotExist:
        return JsonResponse({'hormoon_spuit': None})
