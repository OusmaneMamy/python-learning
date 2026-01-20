def creer_utilisateur(utilisateurs):
    if utilisateurs:
        print("Un utilisateurs existe déjà")
        return False
    else:
        nom = input("Votre nom: ")
        age_str = input("Votre age: ")
        pays = input("Votre pays: ")
        solde_str = input("Votre solde: ")
        print()
        try:
            age = int(age_str)
            solde = float(solde_str)
        except ValueError:
            print("ValueError: Entrer les valeur numerique pour (age et solde)")
            return
        else:
            if age < 0:
                print("Age négatif")
            elif age > 120 :
                print("Age irréaliste")
            else:
                if solde < 0:
                    print("Solde négatif")
                else:
                    utilisateurs['nom'] = nom
                    utilisateurs['age'] = age
                    utilisateurs['pays'] = pays
                    utilisateurs['solde'] = solde


def afficher_profil(utilisateurs):
    for cle, valeur in utilisateurs.items():
        print(f" {cle}: {valeur}")

    age = utilisateurs["age"]
    solde = utilisateurs["solde"]
    if estMajeur(age):
        print(" Majeur")
    else:
        print(" Mineur")
    
    if solde < 0:
        print(" Erreur (impossible)")
    elif solde == 0:
        print(" Aucun crédit")
    elif 0 <= solde < 100:
        print(" Crédit faible")
    else:
        print(" Crédit confortable")
     

def estMajeur(age):
    if age >= 18:
        return True
    return False

def depot(utilisateurs):
    montant_str = input("Le montant à déposer: ")
    try:
        montant = float(montant_str)
    except ValueError:
        print("ValueError: Entrez les valeurs numériques !")
        return
    else:
        solde = utilisateurs["solde"]
        if montant > 0:
            solde += montant
            utilisateurs["solde"] = solde
            print(f"Le nouveau solde est: {solde}")
        else:
            print("Le montant du depot doit etre superieur à (0)")


def retrait(utilisateurs):
    montant_str = input("Le montant à retirer: ")
    try:
        montant = float(montant_str)
    except ValueError:
        print("ValueError: Entrez les valeurs numériques !")
        return
    else:
        solde = utilisateurs["solde"]
        if 0 < montant <= solde :
            print("Retrait effectué avec succes")
            solde -= montant
            utilisateurs["solde"] = solde
            print(f"Votre solde est: {solde}")
        
        elif montant <= 0:
            print("Impossible le montant doit etre superieur à (0)")
        else:
            print("Impossible: solde inférieur au montant")



utilisateurs = {}
while True:
    print("-----------------Menu--------------------")
    print("1. Créer utilisateur")
    print("2. Afficher profil")
    print("3. Deposer de l'argent")
    print("4. Retirer de l'argent")
    print("5. Quitter")

    choix = input("Faites votre choix: ")
    print("----------------------------------------")
    match choix:
        case "1":
            creer_utilisateur(utilisateurs)
        case "2":
            if not utilisateurs:
                print("Veuillez créer un utilisateur d'abord")
            else:
                afficher_profil(utilisateurs)
        case "3":
            if not utilisateurs:
                print("Veuillez créer un utilisateur d'abord")
            else:
                depot(utilisateurs)
        case "4":
            if not utilisateurs:
                print("Veuillez créer un utilisateur d'abord")
            else:
                retrait(utilisateurs)
        case "5":
            break
        case _:
            print("Error de choix !")

