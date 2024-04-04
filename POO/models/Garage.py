from models.Voiture import Voiture

class Garage:
    nombre_places = 0
    nom = ""
    localisation = ""
    liste_vehicule = []
    
    # def __init__(self, places, nom, localisation):
    #     self.nombre_places = places
    #     self.nom = nom
    #     self.localisation = localisation
    #     self.liste_vehicule = []

    def ajouter_voiture(self, vehicule : Voiture):
        if vehicule not in self.liste_vehicule and len(self.liste_vehicule) < self.nombre_places:
            self.liste_vehicule.append(vehicule)

    def retire_voitures(self, vehicule : Voiture):
        if vehicule in self.liste_vehicule:
            self.liste_vehicule.remove(vehicule)

    def details_vehicule(self):
        print("===============================================================")
        for vehicule in self.liste_vehicule:
            print(f"Résumé véhicule:")
            print(f"Propriétaire: {vehicule.proprietaire}")
            print(f"Marque: {vehicule.marque}")
            print(f"Modèle: {vehicule.modele}")
            print(f"Puissance: {vehicule.puissance_kw}")
            print(f"Motorisation: {vehicule.motorisation}")
            print(f"Vitesse Actuelle: {vehicule.vitesse_actuelle}")
            print("===============================================================")
