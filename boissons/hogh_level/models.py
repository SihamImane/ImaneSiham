# Create your models here.
class QuantiteMateirePremiere(models.Model):
    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKEY(
        MatierePremiere,
        on_delete=models.PROTECT,
    )
  class Meta:
        abstract = True


class MatierePremiere(models.Model)
    nom = models.CharField(max_lenght=100)
    stock = models.IntegerField() 
    emprise = models.FloatField()
    #models.ForeignKey(
      #UtilisationMatierePremiere
    models.ManyToManyField(UtilisationMatierePremiere)
    models.ManyToManyField(ApprovisionnementMatierePremiere)
    

class UtilisationMatierePremiere(QuantiteMatierePremiere):
    pass

class ApprovisionnementMatierePremiere(QuantiteMatierePremiere):
    localisation = models.CharField(max_lenght=100)
    prix_unitaire = models.FloatField()
    delais = models.IntegerField()


class Localisation(models.Model):
    nom = models.CharField(max_lenght=100)
    taxes = models.FloatField() 
    prix_m2 = models.FloatField()

class Energie(models.Model):
    nom = models.CharField(max_lenght=100)
    prix = models.FloatField()
    localisation = models.ForeignKey(
        Localisation, on_delete=models.PROTECT,
    )  


class DebitEnergie(models.Model):
    debit = models.FloatField()    
    energie = models.ForeignKey(
        Energie, on_delete=models.PROTECT,
    ) 


class Local(models.Model):
    nom = models.CharField(max_lenght=100)
    localisation = models.ForeignKey(
        Localisation, on_delete=models.PROTECT,
    ) 
    surface = models.FloatField()


class Produit(models.Model):
    nom = models.CharField(max_lenght=100)
    prix_de_vente = models.FloatField()
    quantite = models.FloatField()
    emprise = models.FloatField()
    local = models.ForeignKey(
        Local, on_delete=models.PROTECT,
    ) 

class Metier(models.Model):
    nom = models.CharField(max_lenght=100)
    remuneration = models.FloatField()

class RessourceHumaine(models.Model):
    quantite = models.FloatField()
    metier = models.ForeignKey(
        Metier, on_delete=models.PROTECT,
    ) 

class Machine(models.Model):
    nom = models.CharField(max_lenght=100)
    prix_achat = models.FloatField()
    cout_maintenance = models.FloatField()
    debit = models.FloatField()
    surface = models.FloatField()
    debit_energie = models.ForeignKey(
        DebitEnergie, on_delete=models.PROTECT,
    ) 
    taux_utilisation = models.FloatField()
    local = models.ForeignKey(
        Local, on_delete=models.PROTECT,
    ) 
    operateurs = models.ForeignKey(
        RessourceHumaine, on_delete=models.PROTECT,
        blank=True, null=True, related_name="+",
    )

class Fabrication(models.Model):
    produit = models.ForeignKey(
        Produit, on_delete=models.PROTECT,
    )
    utilisations_matiere_premiere = models.ForeignKey(
        UtilisationMatierePremiere, on_delete=models.PROTECT,
        blank=True, null=True, related_name="+",
    )
    machines = models.ForeignKey(
        Machine, on_delete=models.PROTECT,
        blank=True, null=True, related_name="+",
    )
    ressources_humaines = models.ForeignKey(
        RessourceHumaine, on_delete=models.PROTECT,
        blank=True, null=True, related_name="+",
    )
  
    

    
  

  
  
