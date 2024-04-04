class Elephant:
    nom = ""
    appétit = 0
    satisfaction = 0
    en_vie = True
    soigneur = None

    def manger(self):
        if self.appétit < 100:
            self.appétit += 10
            print(f"{self.nom} vient d'être nouris par {self.soigneur.nom}.")
        else:
            print(f"{self.nom} est déjà comblé.")
