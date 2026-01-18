from datetime import datetime





#Exercice - 4 Age futur
    # Calcul temporel
    # 1. Demande:
        #. année de naissance
    # 2. Calcul:
        #. age actuel (annéé = 2026)
        #. age dans 20 ans 
    # 3. Affiche clairement les résultats


annee_naissance = int(input("Votre année de naissance: "))

annee_actu = datetime.now().year
age_actu = annee_actu - annee_naissance
age_20 = age_actu + 20

print(f"Vous avez: {age_actu} ans")
print(f"Dans 20 ans, vous aurez {age_20} ans")