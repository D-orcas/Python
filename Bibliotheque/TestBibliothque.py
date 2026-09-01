import unittest
from livres import Livre
from livreNumerique import LivreNumerique
from bibliotheques import Bibliotheque
class test_bibliotheque(unittest.TestCase)    :
    def test_nombre_titre(self):
        self.biblio = Bibliotheque()
        l_1 = Livre ("Manigance" ,"Marie-louise", 1890)
        l_2 = LivreNumerique("La petite paulette", "Jean", 290,35)
        l_3 = LivreNumerique("Les enfants perdus", 'Anette' , 467, 342)
        try :
            l_4 = Livre("Le buisson","Paul", 19)
        except ValueError as v :
                print(v)
        l_5 = Livre("Luissante","Marc", 345)
        self.biblio.ajouter_livre(l_1)
        self.biblio.ajouter_livre(l_2)
        self.biblio.ajouter_livre(l_3)
        self.biblio.ajouter_livre(l_4)
        self.biblio.ajouter_livre(l_5)
        self.assertIn("Manigance", self.biblio.titres())



if __name__ == "__main__":
    unittest.main()