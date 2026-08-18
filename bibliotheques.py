import random
from livreNumerique import LivreNumerique
from membre import Membre
from livres import Livre
class Bibliotheque :
    def __init__ (self) :
        self.livres = []
        self.livres_en_cours = [] #Ici on met les livres empruntés et on les supprimes dans self.livres 
        self.liste_membres = []
    def ajouter_membre(self, membre):
        self.liste_membres.append(membre)
        #Qui ajoutes de nouveau memebres à la liste des membres
    def liste_abonne (self) :
        return [i.info_membre() for i in self.liste_membres ]
    #retourne la liste des membres
    def liste_id (self ) :
        return [i.identifiant for i in self.liste_membres ]
    #retourne la liste de ids
    def ajouter_livre (self , livre):
        #On peut l(utiliser pour créer des livres ou supposer que la bibliothèque a payé de nouveaux livres)
        self.livres.append(livre)
    def livre_encours(self) :
        #Pas très important pour l'instant je verrais si je vais le ssupprimer
        return [i.resume() for i in self.livres_en_cours] 
    def ajouter_livre_en_cours(self ,titre) :#cherchons isbn
        for i in self.livres :# Je vais mettre dans la liste du membre aussi mais ce serait dans le main ou comment
            #je sais c'est dans le main car icic c'est la bibliothèque
            if (i.titre == titre.lower()):
                
        #cette méthode prend un livre cherche son isbn dans la liste des livresde la bibliothèque
        #prends ce livre et le supprime de la liste des livres de la bibliothèque mais avan il l'ajoute à la liste de lesvres en cours ou empruntés
                self.livres_en_cours.append(i) # Pour faciliter et si on lui donait juste le titre du livre ? ce serait facile
                self.livres.remove(i)
    def titre_a_livre(self , titre) :
        #La méthode prend un titre et reourne un livre dans les livres enmpruntés
        for i in self.livres_en_cours :
            if (i.titre == titre.lower()) :
                return i #Ici je me demande comment cela marcherai si le livre n'est pas dispo il retourne un null ou nono ou quoi ?
    """@property
    def rechercher_livre(self , titre):
        # Elle recherche un livre dans la bibliothèque et en même temps dans dans les livres empruntés
        for i in self.livres :
            if( i.titre == titre.lower())  :
                print ("le livre ", titre.capitalize() , " est disponible")
                est_disponible = True
                break
        else :
            self.recherche_dans_emprunt(titre)
    def recherche_dans_emprunt(self , titre) :
        livre = self.titre_a_livre(titre)
        if livre in self.livres_en_cours :
            print(f"Le livre : {titre.capitalize()} a été emprunté") 
            est_disponible = False
        else :
            print(f"Le livre {titre.capitalize()} est indisponible")
    def nombre_total_livres (self):
        return len(self.livres)
    #Lorsque la personne donne le titre du livre qu'il recherche
    #on prend l'isbn pour verifier si c'est vraiment le livre qu'il a emprunté
    def supprime_ancien(self , titre) :
        # Avec les titres c'est plus facile pluss besoin de nombre de pages et autres
        for i in self.livres :
            if (i.titre == titre.lower() ):
                self.livres.remove(i)
            else :
                print("Le livre ", titre.capitalize(), " est introuvable")"""
    def recherche_livre(self ,titre) :
        for i in self.livres :
            if( i.titre == titre.lower())  :
                return 1
            else :
                return self.recherche_dans_emprunt(titre)
    def recherche_dans_emprunt(self , titre) :
        livre = self.titre_a_livre(titre)
        if livre in self.livres_en_cours :
            return 2
        else :
            return 0
                    
        # Si l'on suppose que certains livres classiques sont dechirés ou hors d'usage
    def ajoute_retourne(self, title) :
        # Elle ajoute retourné par un abonné un livre par son titre dans la bibliothèque et le supprime de la liste des livres empruntés
        for i in self.livres_en_cours :
            if (i.titre == title.lower())  :
                self.ajouter_livre(i)
                self.livres_en_cours.remove(i) 
                print("Livre ajouté à la bibliothèque")
                break
            else :
                #je vais mettre un sinon pour que le message ne s'affichr pas en boucle mais une seule fois
                #Je continue après je reviens
                print("ce livre n'a pas été emprunté")
                    
    def livres_longs (self):

        return [i.resume() for i in self.livres if i.est_long ]
    def livres_numeriques (self):
        return [i.resume() for i in self.livres if isinstance(i , LivreNumerique)]
    def titres (self) :
        return [i.titre.capitalize() for i in self.livres ]
    def afficher_tout (self):
        for i in self.livres :
            print(i.resume())
    def sauvegarder (self ,nom_fichier) :
        with open (nom_fichier , "w") as fiche :
            for i in self.livres :
                fiche.write(i.resume() + " \n")
    def charger_resumes (self , nom_fichier) :
        with open (nom_fichier, "r") as fiche :
            for i in fiche :
                print (i.strip())
    def livre_aleatoire(self ):
        choix = random.choice(self.livres)
        return choix.resume()
    # random.choice(liste) retourne un élément aléatoire d'une liste
    
                
    


