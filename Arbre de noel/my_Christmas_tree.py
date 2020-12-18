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
christmasBalls = 0
array = []
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


def christmasDecorations(christmasBalls, christmasTinsel)
    nbspaces = heightOfChristmasTree + total
    for i in range (0, heightOfChristmasTree, +1)
        if i == 1 and i == 2:
            christmasBalls = 



# Boucle permettant de répeter le nombre de ligne et agrandir le sapin
while actuel < numberOfRepetition:
    christmasTree(numberOfStars, heightOfChristmasTree, actuel, total)
    actuel += 1
christmasTreesTrunk = ((((nbSpaces+1) * " ") + ("*" * 5) + ((nbSpaces+1) * " ")) * numberOfTrees) # Variable servant a créer le Tronc du Sapin de noel
# christmasTinsel = ((nbSpaces - 4) * "|")
print((christmasTreesTrunk + "\n") * 3)



# mutlipleChristmasTree(numberOfStars, heightOfChristmasTree, actuel, total, numberOfTrees)



