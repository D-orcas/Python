from livres import Livre
class LivreNumerique (Livre) :
    def __init__ (self,titre ,auteur, nombre, taille_mo):
        super().__init__(titre, auteur, nombre)
        self.taille_mo = taille_mo
    def resume (self):
        return super().resume() +f" Fichier numérique de {self.taille_mo} Mo"
