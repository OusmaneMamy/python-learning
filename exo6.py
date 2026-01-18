# Exercice 6 - Depense quotidienne (mini-projet)
    #Application concrète
    #1. Demande
        #. montant du petit-déjeuner
        #. montant du déjeuner
        #. montant du diner
    #2. Calcule:
        #. dépense totale de la journée
    #3. Affiche:


montant_petit_dej = float(input("Entrez le montant du petit déjeuner: "))
montant_dej = float(input("Entrez le montant du déjeuner: "))
montant_diner = float(input("Entrez le montant du diner: "))

depense_tatale = montant_petit_dej + montant_dej + montant_diner

print(f"Dépense totale aujourd'hui : {depense_tatale} GNF")
