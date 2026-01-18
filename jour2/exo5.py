#EXERCICE 5 — Le plus grand nombre
    #Demande deux nombres
    #Affiche le plus grand
    #S’ils sont égaux, affiche : Nombres égaux

nombre_1 = float(input("Entre le premier nombre: "))
nombre_2 = float(input("Entre le deuxieme nombre: "))

if nombre_1 > nombre_2:
    print(f"Le nombre ({nombre_1}) est le plus grand")
elif nombre_1 < nombre_2:
    print(f"Le nombre ({nombre_2}) est le plus grand")
else:
    print("Ces deux nombres sont égaux")