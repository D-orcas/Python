from livres import Livre
from livreNumerique import LivreNumerique
from bibliotheques import Bibliotheque
from membre import Membre
import random
#Avant de bien tester je crée pleins de membres pour verifier bien
#je fais un menu si la personne veut emprunter retourner ou verifier si un livre est dispo une sorte de menu quoi
#ou si elle veut voir la liste de ses emprunts ounsi elle veut voir les livres de la bibliothèque 
#Je vais écrire alors des fonctions pour cela comme inscription et autres

bibliotheque = Bibliotheque()
identifiant = 0


def inscription () :
    global identifiant
    nom = input("Cher nouveau membre veuillez saisir votre nom :")
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
    dernier = input("Le titre du dernier livre")
#le main du programme
print("Bienvenue dans la bibliothèque LECTURE POUR TOUS")
while True :
    print("Entrer :")
    print("1 pour vous inscrire si vous n'êtes pas un membre  \nNB: Notez bien votre identifiant il vous servivra lors des prochaines connexins")
    print("2 pour emprunter un livre")
    print("3 pour rechercher un livre dans la bibliothèque")
    print("4 pour voir votre liste de livres empruntés")
    print("5 pour voir votre identifiant si vous l'avez oublié")
    print("6 pour savoir plus sur la bibliothèque")
    print("7 pour sortir")
    a_faire = input("Faites votre saisie :")
    if (a_faire == 1):
        inscription()
        continue
    elif(a_faire == 2):
        emprunter_livre()
        continue
    elif(a_faire == 3):
        recherche_dans_bibliothque()
        continue
    elif(a_faire == 4) :
        liste_emprunte()
        continue
    elif (a_faire == 5) :
    elif (a_faire == 7):
        break

    #print("Qu'est ce que bibliothèque 'LECTURE POUR TOUS' ?\n La bibliothèque LECTURE POUR TOUS est une initiative privée qui a pour but de satisfaire les personnes curieuses assoifées de nouvelles connaissances de sensation forte.")
    #print("Elle est également là pour vous aider à vous évader dans un monde où vos soucis ne sont que des lointains souvenir ne ce serait ce que pour queleques heures avant de revenir à la réalité")
    #On fait l'insciprtion ou la saisie de l'id
    while True :
        car = input("Etes vous un membre de la bibliothèque ? O/N : ")
        if (car == "O" or car == "o") :
            saisir_id()
            break
        elif(car == "N" or car == "n") :
            inscription()
            break
    #On passe à l'emprunt des livres
    emprunter_livre()
#Test des méthodes
"""l_1 = Livre ("Manigance" ,"Marie-louise", 1890,123)
l_2 = LivreNumerique("La petite paulette", "Jean", 290,35,198)
l_3 = LivreNumerique("Les enfants perdus", 'Anette' , 467, 34,12)
try :
   l_4 = Livre("Le buisson","Paul", 19,78)
except ValueError as v :
     print(v)
l_5 = Livre("Luissante","Marc", 345, 19)
bibliotheque = Bibliotheque()   
liste = [l_1, l_2,l_3,l_4,l_5]
for i in liste :
    bibliotheque.ajouter_livre(i)
i = 1
while (i <= 2) :
    title = input("Le nom du livre : ")
    bibliotheque.ajouter_livre_en_cours(title)
    #je vais verifier si le tire de ce livre n'existe pas dans la bibliothèque
    i += 1
#je teste les methodes recher_livre() ajoouter_ivre_en_cours() , ajoute_retourne et livre_encours
titre = input("Veuillez bien saisir le titre du livre que vous voulez emprunter :")
bibliotheque.rechercher_livre(titre)
#bibliotheque.recherche_dans_emprunt(titre.lower())
bibliotheque.afficher_tout()
bibliotheque.ajoute_retourne(titre)
print(bibliotheque.livre_encours())"""

        