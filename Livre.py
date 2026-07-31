class Livre:
    
    def __init__(self,titre,auteur,nombre_page):
        self.titre = titre
        self.auteur = auteur
        self._nombre_page = nombre_page
    @property
    def nombre_page (self):
        return self._nombre_page
    @nombre_page.setter
    def nombre_page (self, nombre):
        if (nombre <= 0):
            raise ValueError("Le nombre de pages doit être positive")
        self._nombre_page = nombre 

    def resume(self):
        return f"Livre '{self.titre}' par {self.auteur} ({self.nombre_page} pages)"
    @property
    def est_long(self):
        if (self.nombre_page > 300):
            return True
        else :
            return False
    """def modifier_pages(self, nouveau_nombre):
        if (nouveau_nombre <= 0):
            raise ValueError("Le nouveau nombre de page doit être strictement supérieur à 0")
        self.nombre_page = nouveau_nombre"""
        


#une classe livre numerique
class LivreNumerique(Livre):
    #ecrire en CamelCase
    def __init__(self, titre, auteur, nombre_page, taille_mo):
        super().__init__(titre, auteur, nombre_page)
        self.taille_mo = taille_mo
    def resume(self):
        num = super().resume()
        return f"{num}  Fichier numérique de {self.taille_mo} Mo"
#je crée une classe biblithèque
class Bibliotheque:
    def __init__(self):
        self.livres = []
    def ajouter_livre(self,livre):
        self.livres.append(livre)
    def nombre_total_livres(self):
        return len(self.livres)   
    def livres_longs(self):
        return [ajout.resume() for  ajout in self.livres if(ajout.est_long)]
    def afficher_tous(self):
        for i in self.livres:
            print(i.resume(), "\n")
    def livres_numeriques(self):
        return [i.resume() for i in self.livres if isinstance(i, LivreNumerique)]
    def sauvegarder(self, nom_fichier) :
        with open(nom_fichier, "w") as fichier :
            for i in self.livres :
                fichier.write(i.resume()+"\n")
                # ici on fait un + car write( prend un seul argument)
    def charger_resumes(self, nom_fichier) :
        with open (nom_fichier, "r") as fichier :
            for i in fichier :
                print(i.strip())
    def titres(self):
        return [i.titre for i in self.livres]
#je teste les livres classiques
try :
    livre7 = Livre("Dorcas", "Dory", 709)  
    print(livre7.est_long)
    livre7.nombre_page = -145 
    print(livre7.resume())
except ValueError as e:
    print("Erreur", e)
try :
    livre8  = Livre("Flammess", "Maeva", 209)
    print(livre8.est_long)
    livre8.nombre_page = 400
    print(livre8.resume()) 
except ValueError as e:
    print("Erreur ", e)
#je teste la bibliothèque
livre3 =Livre("Je ne suis pas coupable", "Agatha Christie", 198)
livre4 = Livre("Le train bleu", "Agatha Christie", 207)
livre5 = Livre("Rien qu'un rang de perles", "Stacey", 498)
livre6 = Livre("Une femme dans les tourments", "Joelle", 980)
livre2  = Livre("Flammes", "Maeva", 109)
livre = Livre("Dorcas", "Dory", 109) 
lit = [livre, livre2, livre3, livre4, livre5, livre6]
biblio = Bibliotheque()
for i in lit :
    biblio.ajouter_livre(i)
print(biblio.nombre_total_livres())
print(biblio.livres_longs())
biblio.afficher_tous()
biblio.sauvegarder("Gentille.txt")
biblio.charger_resumes("Gentille.txt")

#test livre numérique
livre_num = LivreNumerique("bom","Joachim", 567, 34)
print(livre_num.resume())
  #test de fin  
livre10 = LivreNumerique("C'est ma vie", "Jane", 197, 12)
livre11 = LivreNumerique ("Wow beau","Claude AI", 290,45)
livre13 =Livre("Je ne suis pas coupable", "Agatha Christie", 198)
livre12 = Livre("Le train bleu", "Agatha Christie", 707)
livre14 = Livre ("Tomate", "Jardinier", 2700)


bib = Bibliotheque()
listee = [livre10, livre11,livre12, livre13, livre14]
for i in listee :
    bib.ajouter_livre(i)
print("Livre total " ,bib.nombre_total_livres())
print( "Les livres longs : ",bib.livres_longs())
bib.afficher_tous()
print("Les livresnumériques sont :",bib.livres_numeriques())

