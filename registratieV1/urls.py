"""
URL configuration for registratieV1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.generic import RedirectView


from registratie_planten.views import HomeView, PottingView, DiseaseSearchView, \
    TripsInfestationWijdezettingView, TripsInfestationWeek10View, search_soorten, get_hormoon_spuit, \
    HormoonSpuitView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('oppot-invoeren/', PottingView.as_view(), name='potting'),
    path('ziekte-zoeken/', DiseaseSearchView.as_view(), name='disease_search'),
    path('trips-aantasting-invoegen-wk10/', TripsInfestationWeek10View.as_view(), name='trips_infestation_week10'),
    path('trips-aantasting-invoegen-wijdezetting/', TripsInfestationWijdezettingView.as_view(),
         name='trips_infestation_wijdezetting'),
    path('get-hormoon-spuit/', get_hormoon_spuit, name='get_hormoon_spuit'),
    path('search-soorten/', search_soorten, name='search_soorten'),
    path('hormoon_spuit/', HormoonSpuitView.as_view(), name='hormoon_spuit'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/images/favicon.ico')),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
