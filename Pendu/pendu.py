import random
from faker import Faker
from colorama import Fore
import os

fake = Faker('fr_FR')
random_word = fake.word()

# liste_mots = []

# with open("mots.txt", "r") as fichier:
#     for ligne in fichier:
#         mot = ligne.strip()
#         liste_mots.append(mot.lower())

def nettoyage():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def choisir_mot(liste_mots):
    return random.choice(liste_mots)

def afficher_mot(mot, lettres_devinees):
    affichage = ""
    for lettre in mot:
        if lettre in lettres_devinees:
            affichage += lettre
        else:
            affichage += "_"
    return affichage

def pendu():
    # mot_a_deviner = choisir_mot(liste_mots)
    mot_a_deviner = random_word
    tentatives_restantes = 6
    lettres_devinees = []

    while tentatives_restantes > 0:
        nettoyage()
        color = ""
        if tentatives_restantes == 6:
            color = Fore.LIGHTGREEN_EX
        if tentatives_restantes < 6 and tentatives_restantes >= 3:
            color = Fore.YELLOW
        if tentatives_restantes < 3:
            color = Fore.RED
            
        print(Fore.BLUE + "Bienvenue au jeu du pendu!" + Fore.RESET)
        print(Fore.LIGHTMAGENTA_EX + "Le mot à deviner a " + str(len(mot_a_deviner)) + " lettre(s)\n" + Fore.RESET)
        print(Fore.BLUE + "Mot à deviner:", Fore.LIGHTCYAN_EX + afficher_mot(mot_a_deviner, lettres_devinees) + Fore.RESET)
        print(Fore.BLUE + "Tentatives restantes:", color + str(tentatives_restantes) + Fore.RESET)

        lettre = input(Fore.BLUE + "Devinez une lettre: " + Fore.RESET).lower()

        if len(lettre) != 1 or not lettre.isalpha():
            print(Fore.RED + "Veuillez entrer une seule lettre valide." + Fore.RESET)
            continue

        if lettre in lettres_devinees:
            print(Fore.YELLOW + "Vous avez déjà deviné cette lettre." + Fore.RESET)
            continue

        lettres_devinees.append(lettre)

        if lettre in mot_a_deviner:
            print(Fore.GREEN + "\nBonne devinette!" + Fore.RESET)
            if mot_a_deviner == afficher_mot(mot_a_deviner, lettres_devinees):
                print(Fore.GREEN + "Félicitations! Vous avez deviné le mot:" + Fore.RESET, mot_a_deviner)
                break
        else:
            print(Fore.RED + "\nLa lettre n'est pas dans le mot." + Fore.RESET)
            tentatives_restantes -= 1

    else:
        print(Fore.RED + "\nDésolé, vous avez épuisé toutes vos tentatives. Le mot était:" + Fore.RESET, mot_a_deviner)

pendu()