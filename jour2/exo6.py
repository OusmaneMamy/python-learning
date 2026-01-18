# EXERCICE 6 — Mini-projet : Calculatrice simple
    #Demande :
    #un nombre
    #un opérateur (+, -, *, /)
    #un second nombre

    #Affiche le résultat
    #Si l’opérateur est invalide → message d’erreur
    #Si division par zéro → message d’erreur


nombre_1 = float(input("Entrez le premier nombre: "))
operateur = input("Entrez l'operateur (+, -, *, /): ")
nombre_2 = float(input("Entre le second nombre: "))

if operateur == "+":
    somme = nombre_1 + nombre_2
    print(f"La somme est: {somme}")
elif operateur == "-":
    difference = nombre_1 - nombre_2
    print(f"La difference est: {difference}")
elif operateur == "*":
    produit = nombre_1 * nombre_2
    print(f"La difference est: {produit}")
elif operateur == "/":
    if nombre_2 == 0:
        print("Erreur: Division par zero impossible")
    else:
        division = nombre_1 / nombre_2
        print(f"La difference est: {division}")
