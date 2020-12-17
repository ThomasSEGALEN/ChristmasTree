def creation(drawing, maxWidth,width, incrementation, totalHeight, numberOfBranch):
#creation of the leaves
    height = 4
    baseWidth = width
    spaces = 2*int(maxWidth/2)-width
    for line in range(height):
        if line == 0:
            spaces += (incrementation-1)
        drawing.append([])
        for position in range(spaces):
            drawing[line + totalHeight].append(" ")
        for j in range(width):
            drawing[line + totalHeight].append("")
        for position in range(spaces):
            drawing[line + totalHeight].append(" ")
        spaces -= incrementation
        width += incrementation*2
    numberOfBranch -= 1
    totalHeight +=height
    if numberOfBranch >0:
        creation(drawing, maxWidth, baseWidth+2,incrementation+1, totalHeight, numberOfBranch)