class Soigneur:
    #region Attributs
    _nom = ""
    _date_naissance = ""
    _experience = 0
    _nombre_animaux_responsable = 0
    #endregion
    
    #region getter, setter
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        self._nom = value

    @property
    def date_naissance(self):
        return self._date_naissance

    @property
    def expérience(self):
        return self._experience

    @property
    def nombre_animaux_responsable(self):
        return self._nombre_animaux_responsable
    #endregion
    
    #region Méthodes
    def nourrir(self, animal):
        if animal.en_vie and animal.manger(self.nom):
            # animal.manger(self.nom)
            print(f"{self.nom} nourrit {animal.nom} 🍽️")
        else:
            print(f"L'animal {animal.nom} est mort, il ne peut pas être nourri.")
    
    def entretenir(self, animal):
        if animal.en_vie:
            animal.bonheur = 100
            print(f"{self.nom} entretiens {animal.nom} 💟")
        else:
            print(f"L'animal {animal.nom} est mort, il ne peut pas être entretenu....")
    #endregion