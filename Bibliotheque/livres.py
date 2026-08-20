from datetime import date
class Livre :
    def __init__(self,titre,auteur,nombre_page, isbn):
        self.titre = titre.lower()
        self.auteur = auteur.lower()
        self._nombre_page = nombre_page
        self.isbn = isbn
        self.date_ajout = date.today()
    @property
    def nombre_page (self) :
        return self._nombre_page
    @nombre_page.setter
    def nombre_page (self , valeur):
        if (valeur <= 0):
            raise ValueError ("La valeur doit être positive")
        self._nombre_page = valeur
    def resume (self) :
        return f"Livre '{self.titre.capitalize()}' par {self.auteur.capitalize()} ({self._nombre_page} pages) le {self.date_ajout}"   
    @property
    def est_long (self) :
        if (self._nombre_page > 300):
            return True
        else :
            return False
    