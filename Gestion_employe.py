class Employe :
    def __init__(self, nom, poste , salaire):
        self.nom = nom
        self.poste = poste
        self._salaire = salaire #Ce salaire n'est pas l'attribut d'en bas
    @property # c'est un getter lorqu'on l'apelle et comme pas comme methode mais un attribut il retpurne la valeur du salaire que le livre a
    def salaire(self):
        return self._salaire 
    @salaire.setter # lorsqu'on l'appelle  comme une une méthode également et on lui assigne une valeur il le modifie dans self.salaire employé avec cette condition
    def salaire (self , nombre):
        if( nombre <= 0):
            raise ValueError ("Salut doit être positif")
        self._salaire = nombre
    def resume (self ):
        return f"{self.nom} ({self.poste}) - {self.salaire}€/mois "
    @property
    def est_bien_payes (self):
        if (self.salaire > 3000):
            return True
        else :
            return False
class Manager (Employe):
    def __init__(self, nom, poste, salaire , equiper ):
        super().__init__(nom, poste, salaire)
        self.equipe = equiper
    def resume(self):
        return super().resume() + f"{len(self.equipe)}" 
class Entreprise :
    
    def __init__ (self ):
        self.employes = []
    def ajouter_employe (self , employe):
        self.employes.append(employe)
    def employe_bien_payes(self):
        return [i.resume() for i in self.employes if i.est_bien_payes]
    def sauvegarder (self , nom_fichier):
        lire = []
        with open (nom_fichier, "w") as fiche :
            for i in self.employes :
                fiche.write(i.resume() + "\n")
        with open (nom_fichier, "r") as fiche :
            for i in fiche  :
                lire.append (i.strip()) 
        return lire 

e_1 = Employe("Marie","Dagbago", 15700) 
equipe = ["Jeanne","Prudence","Marc","Fleur"]
equipe2 = ["Richard", "Moise","Komi"]
e_2 = Manager ("Jean", "Kouvi", 700 ,equipe)
try :
    e_3 = Employe("Felix","Tokoin",-6790)
except ValueError as e :
    print (e)
e_4 = Manager("Pauline", "Bè", 19000,equipe2)
entreprise = Entreprise()
liste = [e_1, e_2, e_4]#"_3 n'est pas construit 
for i in liste :
    entreprise.ajouter_employe(i)
print (entreprise.employe_bien_payes())
print (entreprise.sauvegarder("Sauvegarde"))