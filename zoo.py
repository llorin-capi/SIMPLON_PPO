from classes import Zoo, Cage, Animal, Aliment

ZooTycoon = Zoo()                # Création du zoo
ZooTycoon.nom='Zoo Tycoon'

Cage1 = Cage()                   # Création des cages
Cage1.nom='Cage des Kangourous'
Cage2 = Cage()
Cage2.nom='Cage des Crocodiles'
Cage3 = Cage()
Cage3.nom='Cage des Suricates'

ZooTycoon.ajouter_cage(Cage1)   # Ajout des cages dans le zoo
ZooTycoon.ajouter_cage(Cage2)
ZooTycoon.ajouter_cage(Cage3)

ZooTycoon.lister_cages()        # Test du bon ajout des cages

print()

# Création des animaux

Kangourou1 = Animal('Kangourou 1', 'Kangourou', Cage1, 'Proie', 'herbivore')
Kangourou2 = Animal('Kangourou 2', 'Kangourou', Cage1, 'Proie', 'herbivore')
Cage1.lister_animaux()

Crocodile1 = Animal('Crocodile 1', 'Crocodile', Cage2, 'Prédateur', 'carnivore')
Crocodile2 = Animal('Crocodile 2', 'Crocodile', Cage2, 'Prédateur', 'carnivore')
Cage2.lister_animaux()

Suricate1 = Animal('Suricate 1', 'Suricate', Cage3, 'Proie', 'herbivore')
Suricate2 = Animal('Suricate 2', 'Suricate', Cage3, 'Proie', 'herbivore')
Suricate3 = Animal('Suricate 3', 'Suricate', Cage3, 'Proie', 'herbivore')
Suricate4 = Animal('Suricate 4', 'Suricate', Cage3, 'Proie', 'herbivore')
Suricate5 = Animal('Suricate 5', 'Suricate', Cage3, 'Proie', 'herbivore')
Cage3.lister_animaux()

print()

# Prise en compte des relations proie/prédateur
    # lors d'une création d'animal
Suricate6 = Animal('Suricate 6', 'Suricate', Cage2, 'Proie', 'herbivore')
    # lors d'un changement de cage
Suricate5.changer_cage(Cage2)
Crocodile2.changer_cage(Cage1)

print()

#Prise en compte de l'alimentation
carottes = Aliment('les carottes', 'herbivore')
Suricate5.nourrir(carottes)
Crocodile1.nourrir(carottes)
