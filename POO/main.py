from models.Garage import Garage
from models.Voiture import Voiture

if __name__ == "__main__":
    mon_garage = Garage()
    mon_garage.nom = "Technofutur"
    mon_garage.nombre_places = 13
    mon_garage.localisation = "Belgique : Haineaut"
    
    voiture_1 = Voiture()
    voiture_1.proprietaire = "Le T"
    voiture_1.marque = "Dacia"
    voiture_1.modele = "Sandero"
    voiture_1. puissance_kw = 48
    voiture_1.motorisation = "Diesel"
    voiture_1.vitesse_actuelle = "0"
    
    voiture_2 = Voiture()
    voiture_2.proprietaire = "Fabrice"
    voiture_2.marque = "Chevrolet"
    voiture_2.modele = "Impalla SS 67"
    voiture_2. puissance_kw = 96
    voiture_2.motorisation = "Essence"
    voiture_2.vitesse_actuelle = "0"
    
    voiture_3 = Voiture()
    voiture_3.proprietaire = "Eric"
    voiture_3.marque = "Citroen"
    voiture_3.modele = "Ami"
    voiture_3. puissance_kw = 10
    voiture_3.motorisation = "Electrique"
    voiture_3.vitesse_actuelle = "0"
    
    mon_garage.ajouter_voiture(voiture_1)
    mon_garage.ajouter_voiture(voiture_2)
    mon_garage.ajouter_voiture(voiture_3)
    
    mon_garage.details_vehicule()