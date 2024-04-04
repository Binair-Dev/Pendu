from models.Elephant import Elephant


class Soigneur:
    nom = ""
    date_naissance = ""
    experience = ""
    nombre_animaux_responsable = 0
    
    def nourir(self, animal : Elephant):
        animal.manger()
        pass
    
    def entretenir(self, animal : Elephant):
        if animal.satisfaction < 100:
            animal.satisfaction += 10
            print(f"Le soigneur {self.nom} vient de s'occuper de {animal.nom}.")
            print(f"Sa satisfaction vient de grimper de 10% !")
        else:
            print(f"Le soigneur n'a pas besoin de s'occuper de {animal.nom} aujourd'hui.")