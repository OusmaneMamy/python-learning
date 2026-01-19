#  --------------------OBJECTIF---------------------------

# Créer un mini-programme qui :
# Gère un profil utilisateur complet
# Calcule des données financières et scolaires
# Prend des décisions complexes avec conditions imbriquées
# Affiche des résultats clairs pour tous les cas possibles
#     ÉTAPES DU PROGRAMME




# #1. Informations personnelles
#     Demande à l’utilisateur :
#         Nom, prénom
#         Année de naissance
#         Âge → calculé automatiquement
#         Pays
#     Affiche :
#         Nom complet
#         Âge actuel et âge dans 5 ans
#         Mineur / Majeur
#     Message personnalisé selon le pays :
#         Guinée → Bienvenue en Guinée !
#         Autre → Bienvenue !
from datetime import datetime


nom = input("Votre nom: ")
prenom = input("Votre prenom: ")
annee_naissance = int(input("Votre année de naissance: "))
pays = input("Votre pays: ")

annee_actu = datetime.now().year
age_actu = annee_actu - annee_naissance
age_5 = age_actu + 5

print(f"{prenom} {nom}")
print(f"Vous avez {age_actu} ans et dans 5 ans vous aurais ({age_5} ans)")

if age_actu < 18:
    print("Vous etes mineur")
else:
    print("Vous etes majeur")


if pays.capitalize() == "Guinee":
    print(f"Bienvenue en {pays} !")
else:
    print("Bienvenue !")


    
# #2. Gestion financière
# Demande :
#     Salaire mensuel
#     Loyer, nourriture, transport, autres dépenses
# Calcule :
#     Dépenses totales
#     Reste à vivre
# Affiche :
#     Déficit (< 0)
#     Situation critique (0–20% du salaire)
#     Situation stable (> 20%)

salaire  = float(input("Votre salaire mensuel: "))
loyer = float(input("Votre loyer: "))
nourriture = float(input("Votre nourriture: "))
transport = float(input("Votre transport: "))
autres_depenses = float(input("Autres depenses: "))

if salaire <= 0:
    print("Invalide: Le salaire doit etre superieur à (0)")
else:
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

        

# #3. Évaluation académique
#     Demande :
#         Note Maths
#         Note Physique
#         Note Informatique
#     Calcule :
#         Moyenne générale
#     Affiche :
#         Redoublement (<10)
#         Rattrapage (≥10 mais une note <8)
#         Admis (≥10 et toutes ≥8)

note_maths = float(input("Note en maths: "))
note_physique = float(input("Note en physique: "))
note_infos = float(input("Note en informatique: "))

NB_NOTE = 3
somme = note_maths + note_physique + note_infos
moyenne = somme / NB_NOTE

if moyenne <10 :
    print("Redoublement <>")
elif (moyenne >=10 and note_maths < 8) or (moyenne >=10 and note_physique < 8) or (moyenne >=10 and note_infos < 8):
    print("Rattrapge")
else:
    print("Admis")

    

# #4. Analyse de nombres
#     Demande un nombre (entier)
#     Affiche :
#         Positif / Négatif / Nul
#         Pair / Impair
#         Multiple de 5 ou non


nombre = int(input("Entrez un nombre: "))

if nombre > 0:
    print("Positif")
elif nombre <0:
    print("Négatif")
else:
    print("Nul")

if nombre %2 == 0:
    print("Paire")
else:
    print("Impaire")

if nombre / 5 == 0:
    print("Ce nombre est un multiple de 5")
else:
    print("Ce n'est pas un multiple 5")

    

# #5. Mini-système bancaire
#     Demande :
#         Solde
#         Montant à retirer
#     Affiche :
#         Retrait réussi si montant ≤ solde et >0
#         Sinon, message d’erreur précis

solde = float(input("Votre solde: "))
montant = int(input("Entrez le montant à retirer: "))

if montant <= solde and solde >0:
    print("Retrait éffectué avec succes !")
else:
    print("Le montant à rétirer doit etre inférieur au solde")

