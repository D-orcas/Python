from livres import Livre
from livreNumerique import LivreNumerique
from bibliotheques import Bibliotheque
from membre import Membre
import random
#Avant de bien tester je crée pleins de membres pour verifier bien
bib = Bibliotheque()

"""def inscription () :
    nom = input("Cher nouveau membre veuillez saisir votre nom :")
    id_genere = random.randrange(1,9999)
    if id_genere not  in bib.liste_id() :
        identifiant = id_genere
        membre = Membre(nom ,identifiant)
        bib.membre_abonne(membre)
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
    numero = input("Veuillez saisir votre  numéro d'identification :")
    try :
        identifiant = int(numero)
        i = bib.liste_id()
        if identifiant in i :
            print("Identifiant correct !")
        else :
            print("Saisie incorrecte")  
            ressaisir_id()
    except ValueError as v :
        print("Saisie incorrecte :", v)
        





        
            




    
print("Bienvenue dans la bibliothèque LECTURE POUR TOUS")
while True :
    car = input("Etes vous un membre de la bibliothèque ? O/N : ")
    if (car == "O" or car == "o") :
        saisir_id()
        break
    elif(car == "N" or car == "n") :
        inscription()
        break"""

l_1 = Livre ("Manigance" ,"Marie-louise", 1890,123)
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
    i += 1

titre = input("Veuillez bien saisir le titre du livre que vous voulez emprunter :")
bibliotheque.rechercher_livre(titre)
#bibliotheque.recherche_dans_emprunt(titre.lower())
bibliotheque.afficher_tout()
bibliotheque.ajoute_retourne(titre)
print(bibliotheque.livre_encours())

        