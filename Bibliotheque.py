class Livre :
    def __init__(self,titre,auteur,nombre_page):
        self.titre = titre 
        self.auteur = auteur
        self._nombre_page = nombre_page
    @property
    def nombre_page (self) :
        return self._nombre_page
    @nombre_page.setter
    def nombre_page (self , valeur):
        if (valeur <= 0):
            raise ValueError ("La valeur doit être positive")
        self._nombre_page = valeur
    def resume (self) :
        return f"Livre '{self.titre}' par {self.auteur} ({self._nombre_page} pages)"   
    @property
    def est_long (self) :
        if (self._nombre_page > 300):
            return True
        else :
            return False
class LivreNumerique (Livre) :
    def __init__ (self,titre ,auteur, nombre, taille_mo):
        super().__init__(titre, auteur, nombre)
        self.taille_mo = taille_mo
    def resume (self):
        return super().resume() +f" Fichier numérique de {self.taille_mo} Mo"
class Bibliotheque :
    def __init__ (self) :
        self.livres = []
    def ajouter_livre (self , livre):
        self.livres.append(livre)
    def nombre_total_livres (self):
        return len(self.livres)
    def livres_longs (self):
        return [i.resume() for i in self.livres if i.est_long ]
    def livres_numeriques (self):
        return [i.resume() for i in self.livres if isinstance(i , LivreNumerique)]
    def titres (self) :
        return [i.titre for i in self.livres ]
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

l_1 = Livre ("Manigance" ,"Marie-louise", 1890)
l_2 = LivreNumerique("La petite paulette", "Jean", 290,35)
l_3 = LivreNumerique("Le enfants perdus", 'Anette' , 467, 34)
try :
   l_4 = Livre("Le buisson","Paul", -78)
except ValueError as v :
     print(v)
l_5 = Livre("Luissante","Marc", 345)
bibliotheque = Bibliotheque()   
liste = [l_1, l_2,l_3,l_5]
for i in liste :
    bibliotheque.ajouter_livre(i)

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
