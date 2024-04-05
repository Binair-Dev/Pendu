
class Voiture:

#region constructeur
    def __init__(self, proprietaire, marque, modele, puissance_kw, motorisation):
        self._proprietaire = proprietaire
        self._marque = marque
        self._modele = modele
        self._puissance_kw = puissance_kw
        self._motorisation = motorisation
        self._vitesse_actuelle = 0
        self.diametre_pneu = 0.5
#endregion

#region getter, setter
    @property
    def proprietaire(self):
        return self._proprietaire

    # @proprietaire.setter
    # def proprietaire(self, value):
    #     self._proprietaire = value

    @property
    def marque(self):
        return self._marque

    # @marque.setter
    # def marque(self, value):
    #     self._marque = value

    @property
    def modele(self):
        return self._modele

    # @modele.setter
    # def modele(self, value):
    #     self._modele = value

    @property
    def puissance_kw(self):
        return self._puissance_kw

    # @puissance_kw.setter
    # def puissance_kw(self, value):
    #     self._puissance_kw = value

    @property
    def motorisation(self):
        return self._motorisation

    # @motorisation.setter
    # def motorisation(self, value):
    #     self._motorisation = value

    @property
    def vitesse_actuelle(self):
        return self._vitesse_actuelle

    # @vitesse_actuelle.setter
    # def vitesse_actuelle(self, value):
    #     self._vitesse_actuelle = value
    #endregion

#region Props calculé
    @property
    def calcul_rpm(self):
        vitesse_ms = self.vitesse_actuelle / 3.6
        puissance_effective = self.puissance_kw * 0.9
        rpm = ((vitesse_ms) / (3.1459 * self.diametre_pneu)) * (30 / puissance_effective)
        return rpm
#endregion

#region methodes
    def accelerer(self):
        self._vitesse_actuelle += 50

    def freiner(self):
        self._vitesse_actuelle -= 50
#endregion