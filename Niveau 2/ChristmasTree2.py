# Variables declaration
n = 4

# Method1 - Trunk
# stars_nb = 5
# spaces_nb = height - 1
# for i in range(n - 1):
#     for j in range(0, 2):
#         print(spaces_nb * "   " + stars_nb * "*")

# Method2 - Trunk
for i in range(n - 1):
    print("         " + "*****")