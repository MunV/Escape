from django.db import models

class Salle(models.Model):
    nom = models.CharField(max_length=200)
    ressource_type = models.CharField(max_length=200)
    localisation = models.CharField(max_length=200)
    capacite = models.IntegerField(default=1)
     def __str__(self):
        return self.nom

class Reservation(models.Model):
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE)
    titre = models.CharField(max_length=200)
    date_debut = models.DateTimeField('date de debut')
    date_fin = models.DateTimeField('date de fin')
    
    def __str__(self):
        return self.salle
