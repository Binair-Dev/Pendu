import random
from models.Soigneur import Soigneur
class Elephant:
    #region Attributs
    nom = ""
    rassasier = 100
    bonheur = 100
    en_vie = True
    soigneur = Soigneur()
    #endregion
    
    #region getter, setter
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def rassasier(self):
        return self._rassasier

    @property
    def satisfaction(self):
        return self._satisfaction

    @property
    def en_vie(self):
        return self._en_vie

    @property
    def soigneur(self):
        return self._soigneur

    @soigneur.setter
    def soigneur(self, value):
        self._soigneur = value
    #endregion
    
    #region Méthodes
    def manger(self, nom_soigneur):
        if nom_soigneur == self.soigneur.nom:
            self.rassasier = 100
            return True
        else:
            print(f"Le soigneur : {nom_soigneur} n'est pas autorisé a nourir {self.nom}")
    
    def diminuer_rassasier(self):
        self.rassasier -= random.randint(10,30)
        if self.rassasier <= 0:
            self.en_vie = False
            self.rassasier = 0
            self.bonheur = 0
            print(f"{self.nom} est mort de faim ☠️")
    
    def diminuer_bonheur(self):
        self.bonheur -= random.randint(10,20)
        if self.bonheur <= 0:
            self.bonheur = 0
    #endregion