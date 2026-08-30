from bibliotheques import Bibliotheque
from membre import Membre
from livreNumerique import LivreNumerique
from livres import Livre
import random
print("90210")
#Je vais créer des membres pour le test
Maloi =  Membre("Jean-pierre" ,2345)
Maloi2 = Membre("Marielle" , 380)
#Pas besoin de gérer les exceptions car les membres seront crées avec une fonction qui sort les nombres positifs
Maloi3 = Membre("Price" , 108)
#je fais un menu si la personne veut emprunter retourner ou verifier si un livre est dispo une sorte de menu quoi
#ou si elle veut voir la liste de ses emprunts ou si elle veut voir les livres de la bibliothèque 
#Je vais écrire alors des fonctions pour cela comme inscription et autres
#"Persistance : sauvegarde et rechargement de l'état (quels livres sont empruntés par qui) dans un fichier."
bibliotheque = Bibliotheque()
identifiant = 0
global titre 

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
    global identifiant
    try :
        print("****Numéro incorrect! Est-ce une erreur ?*****")
        print("**********Saissez 1 pour réessayer **********")
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
    numero = input("Veuillez saisir votre  numéro d'identification : ")
    try :
        identifiant = int(numero)
        if identifiant in bibliotheque.liste_id() :
            print("Identifiant correct ! ")
        else :
            print("Saisie incorrecte")  
            ressaisir_id()
    except ValueError as v :
        print("Saisie incorrecte : ", v)
#Lorsqu'une personne veut emprunter un livre après avoir donné son identifiant ou être inscrit        

def emprunter_livre ():
  global identifiant
  global titre
  try :  
    while True :
        #print("NB: pour sortir saisissez un caractère quelconque")
        titre = input("Quel est le titre du livre que vous voulez emprunter ? ")
        bibliotheque.rechercher_livre(titre) #Recherche le livre en question
        disponiblite = bibliotheque.recherche_livre(titre)
        if (disponiblite == 1) :
            print("Nous l'ajoutons alors à votre liste d'emprunt ")#Après je remets ceci en commentaire
            livre = bibliotheque.titre_a_livre(titre)
            for i in bibliotheque.liste_membres :
                if (i.identifiant  == identifiant) :
                    i.livre_empruntes(livre)
                    with open ("Bibliotheque.txt" , "w") as f :
                        f.write(livre + " Emprunté par "+ i.nom.capitalize() )
                        # IL faudrai ouvrir le fichier après en le lisant
                    print("Livre ajouté à votre liste d'emprunt")
                    continuer = input ("Voulez vous un autre livre ? O/ N : ")
                    if (continuer == "O" or continuer == "o") :
                        continue 
                    else :
                        remerciemment()
                        break
                     #Plus besoin de else car si la personne est icic c'est que son identifiant est là
        elif (disponiblite == 2 or disponiblite == 0):
            continuer = input("Voulez vous un autre livre ? O/ N : ")
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
  
def recherche_dans_bibliothque():
    titre = input("Saisir le titre du livre que vous recherchez :")
    bibliotheque.rechercher_livre(titre)
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
l_1 = Livre ("Manigance" ,"Marie-louise", 1890)
l_2 = LivreNumerique("La petite paulette", "Jean", 290,35)
l_3 = LivreNumerique("Les enfants perdus", 'Anette' , 467, 342)
try :
   l_4 = Livre("Le buisson","Paul", 19)
except ValueError as v :
     print(v)
l_5 = Livre("Luissante","Marc", 345)

liste = [l_1, l_2,l_3,l_4,l_5]
for i in liste :
    bibliotheque.ajouter_livre(i)


bibliotheque.ajouter_livre_en_cours("LuiSsante")
bibliotheque.ajouter_livre_en_cours("Manigance")
#bibliotheque.rechercher_livre("Pampam")
#print(bibliotheque.livre_encours())
try :
    while True :
        print("Entrer :")
        print("1 pour vous inscrire si vous n'êtes pas un membre  \nNB: Notez bien votre identifiant il vous servira lors des prochaines connexions")
        print("2 pour emprunter un livre")
        print("3 pour rechercher un livre dans la bibliothèque")
        print("4 pour voir votre liste de livres empruntés")
        #print("5 pour voir votre identifiant si vous l'avez oublié")
        print("5 pour savoir plus sur la bibliothèque")
        print("6 pour sortir")
        a_faire = int(input("Faites votre saisie : "))
        if (a_faire == 1): #test validé
            inscription()
            sasie = int(input("Voulez vous continue ? saisissez 1 sinon un autre chiffre "))
            if sasie == 1 :
                continue
            else  :
                break
        elif(a_faire == 2):#Presque validé il faut la saise de l'id avant que ça soit clean
            try :
                
                # saisir_id()#Lorsque la personne dit qu'elle veut 
                #quitter cela ne quitte pas tout donc faire en sorte que quitter sort de programme pas que cela reviennes sur emprunter_livre()
                #Le problème est : lorsque la saisie est éronnée le programme demande la saisie du titre du livre or cela doit commencer de nouveau
                #Donc chercher une solution aussi
                #Y aun soucis dans le emprunter_livre cela fait des choses bizarres je pense qu'il y a une incohérence
                try :
                    emprunter_livre()
                except ValueError as Val :
                    print("Il faut saisir des lettres", Val)    
                continue
            except ValueError as v :
                print("Erreur de saisie ", v)
        elif(a_faire == 3):#Validé
            recherche_dans_bibliothque()
            continuer = input("Voulez vous continuer ? O/N : ")
            if (continuer == "O" or continuer == "o") :
                continue
            else :
                remerciemment ()
                break
            #Demander ensuite s'ils veulent continuer ou pas non ? e serait plus commode non 
        elif(a_faire == 4) :
            liste_emprunte()
        elif (a_faire == 5) :#validé
            print("Qu'est ce que bibliothèque 'LECTURE POUR TOUS' ?\n La bibliothèque LECTURE POUR TOUS est une initiative privée qui a pour but de satisfaire les personnes curieuses assoifées de nouvelles connaissances de sensation forte.")
            print("Elle est également là pour vous aider à vous évader dans un monde où vos soucis ne sont que des lointains souvenir ne ce serait ce que pour queleques heures avant de revenir à la réalité.")
            print("Ici nous vous proposons de divers types de livres allant ds romans d'enquêtes criminels à des sciences fictions sans oublier les romans comiques rien n'est oublie tout pour vous satisfaire.")
            print("Comment la bibliothèque marche-t-elle ?")
            print("Ici vous allez le droit d'emprunter des livres mais avant cela vous devez être memebre c'est à dire un abonné et alors vous utilserait votre id pour vous connecter lors d'un emprunt")
            break
        elif (a_faire == 6):#valid"
            remerciemment()
            break
        else :
            print ("Saisie eronnéé")    
except ValueError as V :    
    print("Erreur de saisie ", V)