from bibliotheques import Bibliotheque
from membre import Membre
import random

#je fais un menu si la personne veut emprunter retourner ou verifier si un livre est dispo une sorte de menu quoi
#ou si elle veut voir la liste de ses emprunts ou si elle veut voir les livres de la bibliothèque 
#Je vais écrire alors des fonctions pour cela comme inscription et autres
#"Persistance : sauvegarde et rechargement de l'état (quels livres sont empruntés par qui) dans un fichier."
bibliotheque = Bibliotheque()
identifiant = 0

def inscription () :
    global identifiant
    nom = input("Cher nouveau membre veuillez saisir votre nom :")
    #après le nom on génère un id
    id_genere = random.randrange(1,9999)
    if id_genere not  in bibliotheque.liste_id() :
        identifiant = id_genere
        membre = Membre(nom ,identifiant)
        bibliotheque.ajouter_membre(membre)
        print("Votre numéro d'identification est ", identifiant)
 
def ressaisir_id():
    try :
        print("****Numéro incorrect! Est-ce une erreur ?*****")
        print("**********Saisssez 1 pour réessayer **********")
        print("2 pour vous inscrire si vous n'êtes pas abonné")
        print("******Tout autre chiffre pour quitter*********")
        choix = int (input("Votre choix : "))
        if (choix == 1 ) :
            saisir_id()
        elif(choix == 2) :
            inscription()
        else :
            print("Merci et bonne journée à vous ")
    except ValueError as v :
        print("Saisie erronée : ", v)

def saisir_id ():
    global identifiant
    numero = input("Veuillez saisir votre  numéro d'identification :")
    try :
        identifiant = int(numero)
        if identifiant in bibliotheque.liste_id() :
            print("Identifiant correct !")
        else :
            print("Saisie incorrecte")  
            ressaisir_id()
    except ValueError as v :
        print("Saisie incorrecte :", v)
#Lorsqu'une personne veut emprunter un livre après avoir donné son identifiant ou être inscrit        

def emprunter_livre ():
  try :  
    while True :
        titre = input("Quel est le titre du livre que vous voulez emprunter ?")
        print("NB: pour sortir saisissez un caractère quelconque")
        bibliotheque.rechercher_livre(titre)
        disponiblite = bibliotheque.recherche_livre(titre)
        if (disponiblite == 1) :
               # print(" Nous l'ajoutons alors à votre liste d'emprunt ")
            livre = bibliotheque.titre_a_livre(titre)
            for i in bibliotheque.liste_membres :
                if (i.idetifiant  == identifiant) :
                    i.livre_empruntes(livre)
                    with open ("Bibliotheque.txt" , "w") as f :
                        f.write(livre + " Emprunté par "+ i.nom.capitalize() )
                    print("Livre ajouté à votre liste d'emprunt")
                    continuer = input ("Voulez vous un autre livre ? O/ N")
                    if (continuer == "O" or continuer == "o") :
                        continue 
                    else :
                        remerciemment()
                        break
                     #Plus besoin de else car si la personne est icic c'est que son identifiant est là
        elif (disponiblite == 2 or disponiblite == 0):
            continuer = input("Voulez vous un autre livre ? O/ N")
            if (continuer == "O" or continuer == "o") :
                continue 
            else :
                remerciemment()
                break
        else :
            remerciemment()
            break
  except ValueError as v :
      print("Erreur", v)
  finally :
      remerciemment()


        #break
    #i += 1
#Si avant d'emprunter un livre la personne cherchait à savoir si le livre est dispo ou pas ?
#  Et après cela cela j met un point (lui dire d'appuyer su run touche quelconque pour sortir du programme à tout instant 

def recherche_dans_bibliothque():
    titre = input("Saisir le titre du livre que vous recherchez :")
    bibliotheque.recherhcer_livre(titre)
#je vais compléter la fonction recher dans b...
def remerciemment () :
    print("Merci d'être passé à la bibliothèque LECTURE POUR TOUS! A la prochaine")

def liste_emprunte():#affiche la liste des livres empruntés par un membre par son id
    print(bibliotheque.livres_emprunte_parmembre(identifiant))
 
def recherche_id():
    input("Quel est votre nom :")
    print("Vous allez nous donner le titre du premier livre et du dernier livre que vous avez emprunté ici ")
    premier = input("Le titre du premier livre  :")
    dernier = input("Le titre du dernier livre")#je fais un liste des retours des fonction et je mets les retours dans une liste avec 2 nombres
    #si on a 1 au debut et 1 à la fin c'est valdé sinon on donne pas l'id
#le main du programme
print("Bienvenue dans la bibliothèque LECTURE POUR TOUS")
while True :
    print("Entrer :")
    print("1 pour vous inscrire si vous n'êtes pas un membre  \nNB: Notez bien votre identifiant il vous servivra lors des prochaines connexins")
    print("2 pour emprunter un livre")
    print("3 pour rechercher un livre dans la bibliothèque")
    print("4 pour voir votre liste de livres empruntés")
    #print("5 pour voir votre identifiant si vous l'avez oublié")
    print("6 pour savoir plus sur la bibliothèque")
    print("7 pour sortir")
    a_faire = input("Faites votre saisie :")
    if (a_faire == 1):
        inscription()
    elif(a_faire == 2):
        saisir_id()
        emprunter_livre()
    elif(a_faire == 3):
        recherche_dans_bibliothque()
    elif(a_faire == 4) :
        liste_emprunte()
    elif (a_faire == 5) :
        print("Qu'est ce que bibliothèque 'LECTURE POUR TOUS' ?\n La bibliothèque LECTURE POUR TOUS est une initiative privée qui a pour but de satisfaire les personnes curieuses assoifées de nouvelles connaissances de sensation forte.")
        print("Elle est également là pour vous aider à vous évader dans un monde où vos soucis ne sont que des lointains souvenir ne ce serait ce que pour queleques heures avant de revenir à la réalité.")
        print("Ici nous vous proposons de divers types de livres allant ds romans d'enquêtes criminels à des sciences fictions sans oublier les romans comiques rien n'est oublie tout pour vous satisfaire.")
        print("Comment la bibliothèque marche-t-elle ?")
        print("Ici vous allez le droit d'emprunter des livres mais avant cela vous devez être memebre c'est à dire un abonné et alors vous utilserait votre id pour vous connecter lors d'un emprunt")
        break
    elif (a_faire == 7):
        remerciemment()
        break

    