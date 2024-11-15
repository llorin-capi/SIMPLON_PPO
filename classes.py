class Zoo:
    def __init__(self):
        self.nom='Zoo'
        self.liste_cages=[]
    def nb_cages(self):
        return len(self.liste_cages)
    def ajouter_cage(self, Cage):
        self.liste_cages.append(Cage.nom)
        return self.liste_cages
    def lister_cages(self):
        print(f"Liste des cages présentes dans {self.nom} :", self.liste_cages)


class Cage:
    def __init__(self):
        self.nom=''
        self.animaux=[]
        self.type=''
    def lister_animaux(self):
        print(f"Liste des animaux présents dans {self.nom} :", self.animaux)
    def ajouter_animal(self,Animal):
        if self.animaux == []:
            self.animaux.append(Animal.nom)
            self.type = Animal.type
            Animal.cage = self
        elif self.type == Animal.type:
            self.animaux.append(Animal.nom)
            Animal.cage = self
        else :
            print (f'Conflit de prédation! {Animal.nom} ne peut être ajouté à {self.nom}!')



class Animal:
    def __init__(self, nom, espece, Cage, type, alimentation):
        self.nom=str(nom)
        self.espece=str(espece)
        self.type=str(type)                  # Prédateur ou proie
        self.alimentation=str(alimentation)
        Cage.ajouter_animal(self)            # Ajout de l'animal à la cage
    
    def changer_cage(self,Cage):
        self.cage.animaux.remove(self.nom)
        if self.cage.animaux == [] :        # Si l'ancienne cage est désormais vide, on retire son type
            self.cage.type = ''

        if Cage.animaux == [] :             # Si la cage est vide, on lui attribut le type de l'animal
            Cage.animaux.append(self.nom)
            Cage.type = self.type
            self.cage = Cage
        elif Cage.type == self.type:        # Si d'autres animaux du même type sont présents, on ajoute l'animal
            Cage.animaux.append(self.nom)
            self.cage = Cage
        else :
            print (f'Conflit de prédation! {self.nom} ne peut pas aller dans {Cage.nom}!')

    def nourrir(self,Aliment):
        if self.alimentation == Aliment.alimentation :                      # Alimentation similaire
            print (f"{self.nom} est heureux! Il adore {Aliment.nom}!")
        elif self.alimentation == 'omnivore':                                # Cas particulier des omnivores
            print (f"{self.nom} est heureux! Il adore {Aliment.nom}!")
        else :                                                              # Mauvaise alimentation
            print (f"{self.nom} boude {Aliment.nom}. Il déteste ça!")
            

class Aliment:
    def __init__(self, nom, alimentation) :
        self.nom = nom
        self.alimentation = alimentation

