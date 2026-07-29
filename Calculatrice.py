
while True:
    print("__Bienvenue cher utilisateur___")
    print("===============================")
    print("==| Mot clé      |   Signe  |==")
    print("==| Addition     |    +     |==")
    print("==|Soustraction  |    -     |==")
    print("==|Multiplication|    *     |==")
    print("==|  Division    |    /     |==")
    print("===============================")
    cle = input("Veuillez saisir le mot clé pour chaque signe de l'opération souhaitée: ")
    print(cle.lower())
    type_n =input("Entrez E si le 1er nombre est un entier et R pour un réel : ")
    while True:
        if (type_n.lower() in ('e','r')):
           if(type_n.lower()== 'e'):
              n1 = int(input("Entrez le premier nombre :"))
              break
           else:
              n1 = float(input("Entrez le premier nombre :"))
              break
        else:
           print ("Erreur !!!")
    type_n = input("Entrez E si le 2e nombre est un entier et R pour un réel : ")
    while True:
        if (type_n.lower() in ('e','r')):
           if(type_n.lower()== 'e'):
              n2 = int(input("Entrez le premier nombre :"))
              break
           else:
              n2 = float(input("Entrez le premier nombre :"))
              break
        else:
           print ("Erreur !!!")
    while True :
        if(cle.lower() in ("addition","soustraction","multiplication","division")):
            if (cle.lower()=="addition"):
                print("L'addition de ",n1," et de ", n2," = ", n1+n2)
                break
            elif(cle.lower() =="soustraction"):
                 print(" La soustraction de ",n2," dans ", n1," = ", n1-n2)
                 break
            elif(cle.lower() =="multiplication"):
                print("La multiplication de ",n1," et de ", n2," = ", n1*n2)
                break
            elif(cle.lower() =="division"):
                print("La division de ",n1," par ", n2," = ", n1/n2)
                break
        else :
            print('Veuillez recommencer')
        break
    print('erreur')
    """1. Le piège critique — trace ce scénario précis :
Dans le tout premier while True (validation de type_n pour n1), imagine que tu tapes "x" au lieu de "e" ou "r".

Le if est faux → on va dans le else → ça affiche "Erreur !!!"
Le while True boucle donc une deuxième fois...
Question : à ce deuxième tour, la variable type_n contient-elle encore "x", ou une nouvelle valeur ? Regarde bien où se trouve la ligne input(...) qui remplit type_n — est-elle dans le while, ou avant lui ?

2. Regarde la toute dernière ligne du programme :

python
print('erreur')

Elle est en dehors du dernier while, donc elle s'exécute toujours, après lui. Fais tourner le programme dans ta tête avec cle = "addition", n1=2, n2=3 : que va afficher le programme, dans l'ordre, ligne par ligne ? Est-ce que ce print('erreur') a un sens ici ?

3. Le tout premier while True: (celui qui contient tout le programme, dès la ligne 1) :
Cherche un break qui lui appartient, à lui. Tu en vois un ? Si non — que se passe-t-il après avoir affiché le résultat du calcul ? Le programme s'arrête, ou recommence direct depuis "Bienvenue..." ? C'est voulu, ou c'est un oubli ?

Réponds à ces 3 points avec ce que tu observes vraiment en traçant le code (pas ce que tu voudrais qu'il fasse). Le point 1 est celui qui peut vraiment bloquer ton programme — sois précise là-dessus. 🔍"""

     

