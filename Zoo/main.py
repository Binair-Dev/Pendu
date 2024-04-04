from models.Enclos import Enclos
from models.Soigneur import Soigneur
from models.Elephant import Elephant


if __name__ == "__main__":
    passer_un_jour = True
    liste_enclos = []
    
    soigneur = Soigneur()
    soigneur.date_naissance = "08/09/1997"
    soigneur.experience = 8
    soigneur.nom = "Brian Van Bellinghen"
    soigneur.nombre_animaux_responsable = 1
    
    elephant = Elephant()
    elephant.nom = "Thibault"
    elephant.appétit = 50
    elephant.satisfaction = 50
    elephant.en_vie = True
    elephant.soigneur = soigneur
    
    enclos = Enclos()
    enclos.nom = "TfTic"
    enclos.capacité_max = 10
    enclos.taille = 2000
    enclos.ajouter_animal(elephant)
    
    liste_enclos.append(enclos)
    
    while(passer_un_jour):
        response = input("Voulez vous passer un jour ? (y/n)")
        if response == "y":
            for e in liste_enclos:
                print(f"Nous venons de passer un jour dans l'enclos {e.nom}.")
                for animal in e.liste_animaux:
                    soigneur = animal.soigneur
                    response2 = input("Voulez vous que les soigneurs nourissent les animaux ? (y/n)")
                    if response2 == "y":
                        soigneur.nourir(animal)
                        response3 = input("Voulez vous que les soigneurs soignent/occupe des animaux ? (y/n)")
                        if response3 == "y":
                            soigneur.entretenir(animal)
                    else:
                        response3 = input("Voulez vous que les soigneurs soignent/occupe des animaux ? (y/n)")
                        if response3 == "y":
                            soigneur.entretenir(animal)
                print(f"Fin de la journée.")
        else:
            passer_un_jour = False
            print("Fin de la simulation.")