# Create your views here.
from django.views.generic import DetailView
from django.http import JsonResponse
from .models import (
    Localisation,
    Energie,
    DebitEnergie,
    ApprovisionnementMatierePremiere,
    Local,
    Machine,
    MatierePremiere,
    Fabrication,
    RessourceHumaine,
    Metier,
    UtilisationMatierePremiere,
    Produit,
)


class JSONDetailView(DetailView):
    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(self.object.json())


class LocalisationDetailView(JSONDetailView):
    model = Localisation


class EnergieDetailView(JSONDetailView):
    Model = Energie


class DebitEnergieDetailView(JSONDetailView):
    Model = DebitEnergie


class ApprovisionnementMatierePremiereDetailView(JSONDetailView):
    Model = ApprovisionnementMatierePremiere


class LocalDetailView(JSONDetailView):
    Model = Local


class MachineDetailView(JSONDetailView):
    Model = Machine


class MatierePremiereDetailView(JSONDetailView):
    Model = MatierePremiere


class FabricationDetailView(JSONDetailView):
    Model = Fabrication


class RessourceHumaineDetailView(JSONDetailView):
    Model = RessourceHumaine


class MetierDetailView(JSONDetailView):
    Model = Metier


class UtilisationMatierePremiereDetailView(JSONDetailView):
    Model = UtilisationMatierePremiere


class ProduitDetailView(JSONDetailView):
    Model = Produit
