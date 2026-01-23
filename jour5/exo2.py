def convertisseur(unite_source, unite_cible, facteur):

    nombre_str = input(f"Entre la valeur à convertir en {unite_cible} ou (q) pour quitter: ")
    if nombre_str == "q":
        return False
    try:
        nombre = float(nombre_str)
    except ValueError:
        print("ValueError: Entrez les valeurs numériques !")
    else:
        resultat = round((nombre * facteur), 2)
        print(f" {nombre} {unite_source} = {resultat} {unite_cible}")
    return convertisseur(unite_source, unite_cible, facteur)



while True:  
    print("--------------Menu---------------")
    print(" 1. Pouces vers Cm")
    print(" 2. Cm vers Pouces")
    print(" 3. Quitter")

    choix = input("Faites votre choix: ")
    match choix:
        case "1":
            convertisseur("pouce", "cm", 2.54)
        case "2":
            convertisseur("cm", "pouce", 0.394)
        case "3":
            break
        case _:
            print("Erreur: Faites un choix valide")
