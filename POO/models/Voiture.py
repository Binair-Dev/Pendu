class Voiture:
    proprietaire = ""
    marque = ""
    modele = ""
    puissance_kw = 0
    motorisation = ""
    vitesse_actuelle = 0
    
    def accelerer(self):
        self.vitesse_actuelle += 50
        
    def freiner(self):
        self.vitesse_actuelle -= 50