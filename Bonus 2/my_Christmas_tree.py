######## Stars per level
# 1 - 3 - 5 - 7
# 3 - 7 - 11 - 15
# 5 - 11 - 17 - 23


# Les variables pour la fonction christmasTree
numberOfTrees = int(input("Nomber d'arbre de noel : ")) # Variable permattant de créer plusieurs sapin de noel identique
heightOfChristmasTree = int(input("Hauteur de l'arbre de noel : ")) # Variable correspondant a la hauteur du sapin (soit le nombre de ligne qu'il aura)
numberOfRepetition = int(input("Nombre de repetitions : ")) # Variable correspondant au nombres de répetitions de la hauteur du sapin
actuel = 0 # permettre d'indenter la boucle et le pour
numberOfStars = 0 # Le nombre d'etoile a imprimer
total = heightOfChristmasTree * numberOfRepetition #Variable correspondant
nbSpaces = total # Assignation de la variable nbspaces en dehors de la fonction
space = " " # Variable String pour espace
star = "*" # Variable String pour une etoile
star_space = "* " # Variable String pour une etoile + un espace
tinselPipe = "| " # Variable String l'accroche de la guirlande
tinselPipe2 = " |" # Variable String l'accroche de la guirlande
tinselBall = " 0" # Variable String pour un espace + une boule de noel
tinselBalls2 = "0 " # Variable String une boule de noel + pour un espace 
tinselBalls3 = "0" # Variable String pour une boule de noel
nbSpace2 = 0 # Variable int pour le nombre d'espaces
nbSpace3 = 0 # Variable int pour le nombre d'espaces
trunk = "*****" # Variables String pour le tronc du sapin


# Fonction qui créer un arbre de noel de la taille qu'on veut
def christmasTree(numberOfStars, heightOfChristmasTree, actuel, total):
    nbSpaces = heightOfChristmasTree + total
    for i in range(0, heightOfChristmasTree, + 1):        
        if actuel == 0:
            numberOfStars = 1 + (2 * (i))
            nbSpaces -= 1
        else:
            numberOfStars = 1 + (2 * (actuel + 1) * (i)) + (2 * actuel)
            nbSpaces -= (actuel + 1)
        print((nbSpaces * " ") + (numberOfStars * "*"))   

#Fonction pour créer plusieurs sapin (sans tronc et decorations mais fonctionnel)
def multipleChristmasTree(numberOfStars, heightOfChristmasTree, actuel, total, numberOfTrees):
    nbSpaces = heightOfChristmasTree + total

    for i in range(0, heightOfChristmasTree, + 1):
        if actuel == 0:
            numberOfStars = 1 + (2 * (i))
            nbSpaces -= 1
        else:
            numberOfStars = 1 + (2 * (actuel + 1) *(i)) + (2 * actuel)
            
            nbSpaces -= (actuel + 1)
        print(((nbSpaces * " ") + (numberOfStars * "*") + (nbSpaces * " ")) * numberOfTrees)




# def christmasDecorations(christmasBalls, christmasTinsel)
#     nbspaces = heightOfChristmasTree + total
#     for i in range (0, heightOfChristmasTree, +1)
#         if i == 1 and i == 2:
#             christmasBalls

# Calcule le centre de l'arbre
nbSpace2 = ((((numberOfRepetition * 2 - 1) + numberOfRepetition * 2 * 3) / 2))
nbSpace3 = round(nbSpace2)
nbOfTrunks = nbSpace3 - 3
half = (nbSpace3 - 3) / 2
half2 = round(half)


#####CHRISTMAS STAR######
# number_of_space3 = number_of_space2-7
# print(number_of_space3 * space, star, space * 3, star, space * 3, star )

# number_of_space3 = number_of_space2 - 5
# print(number_of_space3 * space, star, space, star, space, star )

# number_of_space3 = number_of_space2 - 1
# print(number_of_space3 * space, star)

# number_of_space3 = number_of_space2 - 5
# print(number_of_space3 * space, star_space * 5)

# number_of_space3 = number_of_space2 - 1
# print(number_of_space3 * space,star)

# number_of_space3 = number_of_space2 - 5
# print(number_of_space3 * space, star, space, "|", space, star )

# number_of_space3 = number_of_space2 - 7
# print(number_of_space3 * space, star, space * 3, "|", space * 3, star )

# number_of_space3 = number_of_space2 - 1


# Boucle permettant de répeter le nombre de ligne et agrandir le sapin
while actuel < numberOfRepetition:
    christmasTree(numberOfStars, heightOfChristmasTree, actuel, total)
    actuel += 1
    # Boucle pour ajouter les guirlandes
    while actuel == numberOfRepetition:
            nbSpaces = total 
            print((("     ") + tinselPipe * half2 + trunk + tinselPipe2 * half2))
            print((("     ") + tinselBalls2 * half2 + trunk + (tinselBall * half2)) )
            print((("    ") + nbOfTrunks* space + trunk))
            actuel += 1
#christmasTree(numberOfStars, heightOfChristmasTree, actuel, total, numberOfTrees)
# print("   ", garland_pipe2 * half2, trunk, garland_pipe * half2)
# print("   ", garland_balls * half2, trunk, garland_balls2 * half2)
# print("  " , number_of_space_trunk * space, trunk)


