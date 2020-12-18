# for i in range (0, 24):     # 23 + 2 marge
#     for j in range (0, 21): # 22

# height = 5
# nbOfBranches = 3
# spacesNb = nbOfBranches * (height - 1)
# starsNb = 1
# nb = 1

# for i in range(height - 1):
#     print(spacesNb * "a" + (i + starsNb) * "*" + spacesNb * "z")
#     starsNb += 1 * nb
#     spacesNb -= 1 * nb
#     print(starsNb)
#     print(spacesNb)
# nb += 1

# print("")

# nbOfBranches = 2
# for i in range(height - 1):
#     print((spacesNb + 3) * "a" + (i*2 + starsNb - 2) * "*" + (spacesNb + 3) * "z")
#     starsNb += 2
#     spacesNb -= 2
#     print(starsNb)
#     print(spacesNb)

# print("")

# for i in range(height - 1):
#     print((spacesNb + 7) * "a" + ((i*1 + starsNb - 8) * "*" + (spacesNb + 7) * "z"))
#     starsNb += 4
#     spacesNb -= 4



height = 4
nbOfBranches = 3
branch = 0
starsNb = 1
spacesNb = nbOfBranches * (height - 1)
var = 0

for i in range(nbOfBranches):
    for j in range(height):
        print((j + starsNb - i*2) * "*")
        starsNb += 1 + branch
        if branch <= 0:
            branch = 0
        else:
            branch += nbOfBranches - 1
            
print("")