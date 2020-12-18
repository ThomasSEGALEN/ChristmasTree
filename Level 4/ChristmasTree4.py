# Stars per level
# 1 - 3 - 5 - 7
# 3 - 7 - 11 - 15
# 5 - 11 - 17 - 23

# Variables declaration
n = 4
height = n

# Method - Stage 1
stars_nb = 1
spaces_nb = height - 1
for i in range(height):
    print("        " + spaces_nb * " " + stars_nb * "*")
    stars_nb += 2
    spaces_nb -= 1

# Method - Stage 2 / Christmas balls
stars_nb = 3
spaces_nb = height - 1
for i in range(height):
    if stars_nb == 3:
        print("     " + spaces_nb * " " + "0 " + stars_nb * "*" + " 0")
        stars_nb += 4
        spaces_nb -= 1
    else:
        print("    " + spaces_nb * "  " + stars_nb * "*")
        stars_nb += 4
        spaces_nb -= 1

# Method - Stage 3 / Christmas balls
stars_nb = 5
spaces_nb = height - 1
for i in range(height):
    if stars_nb == 5:
        print(spaces_nb * " " + " 0    " + stars_nb * "*" + "    0")
        stars_nb += 6
        spaces_nb -= 1
    else :
        print(spaces_nb * "   " + stars_nb * "*")
        stars_nb += 6
        spaces_nb -= 1

# Method - Garland
stars_nb = 5
spaces_nb = height - 1
for i in range(height - 1):
    if i == 0 :
        for j in range(1, 14):      #  Printing when j is equal to...
            if j < 5 :
                print(" |", end="")
            elif j >= 5 and j <= 9 :
                if j == 5 :
                    print(" *", end="")
                else :
                    print("*", end="")
            else :
                print(" |", end="")
    elif i == 1 :
        print("")
        for j in range(1, 14):      #  Printing when j is equal to...
                if j < 5 :
                    print(" 0", end="")
                elif j >= 5 and j <= 9 :
                    if j == 5 :
                        print(" *", end="")
                    else :
                        print("*", end="")
                else :
                    print(" 0", end="")
    else :      #  Printing the trunk
        print("")
        for i in range(height - 3):
		        print(spaces_nb * "   " + stars_nb * "*")