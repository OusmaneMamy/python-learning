#EXERCICE 4 — Mot de passe
    #Demande un mot de passe
    #Si le mot de passe est "python123"

        #Affiche : Accès autorisé
        #Sinon :
        #Accès refusé

MOT_DE_PASSE = "python123"

mot_de_passe_util = input("Entre le mot de passe: ")

if mot_de_passe_util == MOT_DE_PASSE:
    print("Accès autorisé")
else:
    print("Accès refusé")