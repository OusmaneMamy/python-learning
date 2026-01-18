# EXERCICE 3 — Note scolaire
    #Demande une note sur 20
    #Affiche :

        # < 10 → Échec
        # 10 à 12 → Passable
        # 13 à 15 → Bien
        # ≥ 16 → Très bien

note = int(input("Entrez la note: "))

if note < 10:
    print("Echec")
elif 10 < note < 12:
    print("Passable")
elif 13 < note < 15:
    print("Bien")
else:
    print("Trien bien")
