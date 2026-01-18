# EXERCICE 2 — Nombre pair ou impair

    #Demande un nombre
    #Affiche :

        #Nombre pair
        #Nombre impair


nombre = int(input("Entrez un nombre: "))

if nombre % 2 == 0:
    print(f"le nombre {nombre} est pair")
else:
    print(f"le nombre {nombre} est impair")