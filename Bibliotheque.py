"""import random

    
    
   

    



print (bibliotheque.nombre_total_livres())
print (bibliotheque.livres_longs ())
print (bibliotheque.livres_numeriques())
print(bibliotheque.titres())
bibliotheque.afficher_tout()
bibliotheque.sauvegarder("Param")
try :
   bibliotheque.charger_resumes("Param")
except FileNotFoundError as f :
    print( "Erreur ",f)
finally :
    print("Merci à bientôt cher utilisateur")
print(bibliotheque.livre_aleatoire())"""



"""#On fait l'insciprtion ou la saisie de l'id
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
    #je vais verifier si le tire de ce livre n'existe pas dans la bibliothèque
    i += 1
#je teste les methodes recher_livre() ajoouter_ivre_en_cours() , ajoute_retourne et livre_encours
titre = input("Veuillez bien saisir le titre du livre que vous voulez emprunter :")
bibliotheque.rechercher_livre(titre)
#bibliotheque.recherche_dans_emprunt(titre.lower())
bibliotheque.afficher_tout()
bibliotheque.ajoute_retourne(titre)
print(bibliotheque.livre_encours())"""

        
