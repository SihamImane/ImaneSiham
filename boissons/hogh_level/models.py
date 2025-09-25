from django.db import models


class MatierePremiere(models.Model):
    nom = models.CharField(max_length=100)
    stock = models.IntegerField()
    emprise = models.FloatField()

    def __str__(self):
        return f"{self.nom} (stock: {self.stock}, emprise: {self.emprise})"


class QuantiteMatierePremiere(models.Model):
    quantite = models.IntegerField()
    matiere_premiere = models.ForeignKey(
        MatierePremiere,
        on_delete=models.PROTECT,
    )

    class Meta:
        abstract = True


class UtilisationMatierePremiere(QuantiteMatierePremiere):
    def __str__(self):
        return f"Utilisation {self.quantite} de {self.matiere_premiere.nom}"


class ApprovisionnementMatierePremiere(QuantiteMatierePremiere):
    localisation = models.CharField(max_length=100)
    prix_unitaire = models.FloatField()
    delais = models.IntegerField()

    def __str__(self):
        return f"Approvisionnement {self.quantite} {self.matiere_premiere.nom} à {self.localisation}"


class Localisation(models.Model):
    nom = models.CharField(max_length=100)
    taxes = models.FloatField()
    prix_m2 = models.FloatField()

    def __str__(self):
        return f"{self.nom} (taxes: {self.taxes}, prix/m²: {self.prix_m2})"


class Energie(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.FloatField()
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.nom} ({self.prix} €/unité)"


class DebitEnergie(models.Model):
    debit = models.FloatField()
    energie = models.ForeignKey(
        Energie,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.debit} unités de {self.energie.nom}"


class Local(models.Model):
    nom = models.CharField(max_length=100)
    localisation = models.ForeignKey(
        Localisation,
        on_delete=models.PROTECT,
    )
    surface = models.FloatField()

    def __str__(self):
        return f"{self.nom} ({self.surface} m², {self.localisation.nom})"


class Produit(models.Model):
    nom = models.CharField(max_length=100)
    prix_de_vente = models.FloatField()
    quantite = models.FloatField()
    emprise = models.FloatField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.nom} (vente: {self.prix_de_vente}€, quantité: {self.quantite})"


class Metier(models.Model):
    nom = models.CharField(max_length=100)
    remuneration = models.FloatField()

    def __str__(self):
        return f"{self.nom} (rémunération: {self.remuneration}€)"


class RessourceHumaine(models.Model):
    quantite = models.FloatField()
    metier = models.ForeignKey(
        Metier,
        on_delete=models.PROTECT,
    )

    def __str__(self):
        return f"{self.quantite} x {self.metier.nom}"


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix_achat = models.FloatField()
    cout_maintenance = models.FloatField()
    debit = models.FloatField()
    surface = models.FloatField()
    debit_energie = models.ForeignKey(
        DebitEnergie,
        on_delete=models.PROTECT,
    )
    taux_utilisation = models.FloatField()
    local = models.ForeignKey(
        Local,
        on_delete=models.PROTECT,
    )
    operateurs = models.ForeignKey(
        RessourceHumaine,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="+",
    )

    def __str__(self):
        return f"{self.nom} (prix: {self.prix_achat}€, local: {self.local.nom})"


class Fabrication(models.Model):
    produit = models.ForeignKey(
        Produit,
        on_delete=models.PROTECT,
    )
    utilisations_matiere_premiere = models.ForeignKey(
        UtilisationMatierePremiere,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="+",
    )
    machines = models.ForeignKey(
        Machine,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="+",
    )
    ressources_humaines = models.ForeignKey(
        RessourceHumaine,
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name="+",
    )

    def __str__(self):
        return f"Fabrication de {self.produit.nom}"

