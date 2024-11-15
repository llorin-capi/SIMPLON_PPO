from classes import Zoo, Cage, Animal, Aliment

# Initialisation du zoo
print("Bienvenue dans la simulation de zoo!")
zoo = Zoo(input("Veuillez choisir un nom pour votre zoo : "))

# Création du menu interactif
def menu():
    print("\n--- Menu du Zoo ---")
    print("1. Ajouter une cage")
    print("2. Lister les cages")
    print("3. Ajouter un animal à une cage")
    print("4. Lister les animaux d'une cage")
    print("5. Nourrir un animal")
    print("6. Quitter")

# Programme de simulation de zoo
def appli():
    while True:
        menu()
        choix = input("Entrez le numéro de l'action souhaitée : ")
        
        # Ajouter une cage
        if choix == "1":
            nom_cage = input("Entrez le nom de la nouvelle cage : ")
            if nom_cage not in [cage.nom for cage in zoo.cages] : # On vérifie qu'aucune cage ne porte le même nom
                nouvelle_cage = Cage()
                nouvelle_cage.nom = nom_cage
                zoo.ajouter_cage(nouvelle_cage)
                print(f"{nom_cage} a été ajoutée au zoo.")
            else :
                print("Impossible de créer la cage : une cage porte déjà ce nom!")
        
        # Lister les cages
        elif choix == "2": 
            zoo.lister_cages()
        
        # Ajouter un animal à une cage
        elif choix == "3":
            if zoo.cages == []: # On vérifie que le zoo contient des cages
                print("Aucune cage n'est disponible. Ajoutez une cage d'abord.")
                continue
            nom_cage = input("Entrez le nom de la cage où ajouter un animal : ") 
            if nom_cage not in [cage.nom for cage in zoo.cages]: # On vérifie que la cage existe
                print(f"Aucune cage nommée '{nom_cage}' trouvée.")
                continue
            espece = input("Entrez l'espèce de l'animal : ")
            nom_animal = input("Entrez le nom de l'animal : ")
            type_animal = input("Est-ce un prédateur ou une proie ? : ").lower()
            alimentation = input("Entrez le régime de l'animal (herbivore/carnivore/omnivore): ")
            
            # Cherche l'instance de la cage pour l'ajout
            for cage in zoo.cages:
                if cage.nom == nom_cage:
                    animal = Animal(nom_animal, espece, cage, type_animal, alimentation)
                    if animal in cage.animaux :
                        print(f"L'animal '{nom_animal}' a été ajouté dans la cage '{nom_cage}'.")
                    else : 
                        print("Animal non créé.")
                    break
        
        # Lister les animaux d'une cage
        elif choix == "4":
            nom_cage = input("Entrez le nom de la cage : ")
            for cage in zoo.cages:
                if cage.nom == nom_cage:
                    cage.lister_animaux()
                    break
            else:
                print(f"Aucune cage nommée '{nom_cage}' trouvée.")
        
        # Nourrir un animal
        elif choix == "5":
            nom_animal = input("Entrez le nom de l'animal à nourrir : ")
            nom_aliment = input("Entrez le nom de l'aliment : ")
            regime = input("Entrez le régime correspondant de l'aliment (herbivore/carnivore): ")

            aliment = Aliment(nom_aliment, regime)  # Création de l'aliment
            for cage in zoo.cages:
                for animal in cage.animaux:
                    if animal.nom == nom_animal:
                        animal.nourrir(aliment)
                    break
                else:
                    continue
                break
            else:
                print(f"Animal '{nom_animal}' introuvable.")
        
        elif choix == "6":
            print("Merci d'avoir utilisé le gestionnaire de Zoo. À bientôt !")
            break
        
        else:
            print("Choix invalide, veuillez réessayer.")

# Lancer le programme
appli()