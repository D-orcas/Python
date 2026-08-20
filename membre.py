class Membre :
    def __init__(self, nom , identifiant):
        #conversion en minuscule 
        self.nom = nom.lower()
        self.identifiant = identifiant
        self.livre_emprunte = []
    def info_membre (self) :
        return f"Nom : {self.nom.capitalize()} numéro d'identification : {self.identifiant} liste des livres empruntés depuis l'abonnement :{self.liste_livre_emprunte}"
    def livre_empruntes (self, livre) :
        self.livre_emprunte.append(livre)#Ajoute des livres à la liste des livres empruntés
    @property
    def liste_livre_emprunte(self):#La liste des livres empruntés pour que la liste soit bien lisible
        return [i for i in self.livre_emprunte]  