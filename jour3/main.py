"""
Mini projet Python — Jour 3

Objectifs :
- Gestion de profil utilisateur
- Calculs financiers et académiques
- Prise de décision avec conditions imbriquées
- Menu interactif

Auteur : Ousmane Pe Mamy
"""

from datetime import datetime



def gestion_profil():
    nom = input("Votre nom: ")
    prenom = input("Votre prenom: ")
    annee_naissance = int(input("Votre année de naissance: "))
    pays = input("Votre pays: ")

    annee_actu = datetime.now().year
    age = annee_actu - annee_naissance
    age_5 = age + 5

    print()
    print(f"{prenom} {nom}")
    print(f"Vous avez {age} ans et dans 5 ans vous aurais ({age_5} ans)")

    if estMajeur(age):
        print("Vous etes majeur")
    else:
        print("Vous etes mineur")

    if messagePersonnaliser(pays):
        print(f"Bienvenue en {pays} !")
    else:
        print("Bienvenue !")

def estMajeur(age):
    if age >= 18:
        return True
    return False

def messagePersonnaliser(pays):
    if pays.capitalize() == "Guinee":
       return True
    return False

    
def gestion_financier():
    salaire  = float(input("Votre salaire mensuel: "))

    while True:
        if salaire <= 0:
            print("Error: le salaire doit etre superieur à (0)")
            salaire  = float(input("Votre salaire mensuel: ")) 
        else:
            loyer = float(input("Votre loyer: "))
            nourriture = float(input("Votre nourriture: "))
            transport = float(input("Votre transport: "))
            autres_depenses = float(input("Autres depenses: "))
            depenses_totales = loyer + nourriture + transport + autres_depenses
            reste = salaire  - depenses_totales
            salaire_poucent = (salaire  * 20) /100
            print(f"Dépense: {depenses_totales}")
            print(f"Reste à vivre: {reste}")

            if reste < 0:
                print("Vous été en déficit")
            elif  0 <= reste <= salaire_poucent:
                print("Situation critique")
            elif reste > salaire_poucent:
                print("Situation stable")
            break
  

def evaluation_academique():
    note_maths = float(input("Note en maths: "))
    note_physique = float(input("Note en physique: "))
    note_infos = float(input("Note en informatique: "))

    somme = note_maths + note_physique + note_infos
    moyenne = moyennes(somme)
    if moyenne <10 :
        print("Redoublement <>")
    elif (moyenne >=10 and note_maths < 8) or (moyenne >=10 and note_physique < 8) or (moyenne >=10 and note_infos < 8):
        print("Rattrapge")
    else:
        print("Admis")

def moyennes(somme):
    NB_NOTE = 3
    moyenne = somme / NB_NOTE
    return moyenne


def mini_banque():
    solde = float(input("Votre solde: "))
    
    while True:
        if solde  <= 0:
            print("Le solde doit etre superieur à 0.")
            solde = float(input("Votre solde: "))
        else:
            montant = float(input("Entrez le montant à retirer ou (0) pour quitter: "))
            if montant == 0:
                break
            if ( 0 < montant < solde ):
                print("Retrait éffectué avec succes !")
                solde = solde - montant
                print(f"Votre nouveau solde est: {solde}")
            elif montant <= 0:
                print("Error: le montant à retirer doit etre supperieur à (0)")
            else:
                print("Error: Votre solde est insuffiansant pour ce montant!")
            

while True:
    print("--------------Menu-----------------")
    print("1. Profil")
    print("2. Finance")
    print("3. Scolarité")
    print("4. Banque")
    print("0. Quitter")

    choix= input("Faites un choix: ")
    match choix:
        case "0":
            break
        case "1":
            gestion_profil()
        case "2":
            gestion_financier()
        case "3":
            evaluation_academique()
        case "4":
            mini_banque()
        case _:
            print("Erreur de choix !")
        

