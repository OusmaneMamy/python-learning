#Exercice 3 - Conversion
    #Calcul + logique simple
    #1. Demande une température en Celsius
    #2. Convertis-la en Fahrenheit

temp_celsius = float(input("Entrez la température en celsius: "))

f = round(((temp_celsius * (9/5)) + 32), 2)
print(f"{temp_celsius} Celsius = {f} Fahrenheit")