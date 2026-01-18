# Exercice 5 - Nombre magique
    #Manipulation d'un nombre
    #1. Demande un nombre
    #2. Affiche:
        #. son double
        #. son triple
        #. son carré
        #. son cube

nombre = int(input("Entre un nombre: "))

print(f"Le double de {nombre} est: {nombre * 2}")
print(f"Le triple de {nombre} est: {nombre * 3}")
print(f"Le carré de {nombre} est: {nombre ** 2}")
print(f"Le cube de {nombre} est: {pow(nombre, 3)}")
