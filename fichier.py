with open("Mon", "w") as fich :
    fich.write("Le train bleu \n")
    fich.write("Le dernier énigme")
with open("Mon", "r") as fich :
    amele = fich.read()
    #hihi amélé comme moi
    print(amele)
with open("Mon", "r") as fich :
    for i in fich :
        print(i)
try :
    with open ("Mon_jeu","r") as fiche :
        amande = fiche.read()
        print(amande)
except Exception as e:
    #Parcontre il faut préciser le type d'erreur pour que si d'autres erreurs s'y glissent 
    # il va pas aficher seulemnt erreur
    print("Erreur")