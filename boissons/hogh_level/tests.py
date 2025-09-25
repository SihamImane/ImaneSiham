# Create your tests here.
from django.test import TestCase
from .models import Metier
from .models import (Localisation, RessourceHumaine, Energie, DebitEnergie, ApprovisionnementMatierePremiere, Local, Machine, MatierePremiere)

class MetierModelTests(TestCase):
   def test_metier_creation(self):
       self.assertEqual(Metier.objects.count(), 0)
       Metier.objects.create(nom="Automaticien", remuneration=2800)#, cout_maintenance=1000, debit=1500, surface=20, debit_energie=None)
       self.assertEqual(Metier.objects.count(), 1)




class LocalisationModelTest(TestCase):
    def test_localisation_creation(self):

        self.assertEqual(Localisation.objects.count(), 0)
        loca=Localisation.objects.create(nom="Lyon", taxes=2000, prix_m2=1000)
        loca2=Localisation.objects.create(nom="Labege", taxes=2000, prix_m2=2000)

        self.assertEqual(Local.objects.count(), 0)
        loca3=Local.objects.create(nom="locstock", localisation=loca2, surface=50)

        self.assertEqual(Machine.objects.count(), 0)
        Machine.objects.create(nom="Mach1", prix_achat=1000, cout_maintenance=1000, debit=1500, surface=20, debit_energie=None, taux_utilisation=50, local=loca3, operateurs=None)
        Machine.objects.create(nom="Mach2", prix_achat=2000, cout_maintenance=1000, debit=1500, surface=20, debit_energie=None, taux_utilisation=50, local=loca3, operateurs=None)

        self.assertEqual(MatierePremiere.objects.count(), 0)
        MatierePremiere.objects.create(nom="sucre", stock=1000, emprise=None)
        MatierePremiere.objects.create(nom="eau", stock=50, emprise=None)
 
        self.assertEqual(ApprovisionnementMatierePremiere.objects.count(), 0)
        ApprovisionnementMatierePremiere.objects.create(nom="electricite", prix=20, localisation=loca)

        self.assertEqual(Energie.objects.count(), 0)
        en=Energie.objects.create(nom="electricite", prix=20, localisation=loca)

        #en.costs()
        self.assertEqual(DebitEnergie.objects.count(), 0)
        cc=DebitEnergie.objects.create(debit=100, energie=en)
        self.assertEqual(DebitEnergie.objects.count(), 1)
        cc.costs()
