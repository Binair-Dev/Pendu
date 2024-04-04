class Enclos:
    nom = ""
    capacité_max = 0
    taille = 0
    liste_animaux = []

    def ajouter_animal(self, animal):
        if len(self.liste_animaux) < self.capacité_max:
            self.liste_animaux.append(animal)

    def enlever_animal(self, animal):
        if animal in self.liste_animaux:
            self.liste_animaux.remove(animal)

    def afficher_animaux(self):
        print("Animaux dans l'enclos :")
        for animal in self.liste_animaux:
            print(animal)
