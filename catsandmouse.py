def catAndMouse(x, y, z):
    catA = abs(x-z)
    catB = abs(y-z)
    if (catA < catB):
        return "Cat A"
    elif (catB < catA):
        return "Cat B"
    else:
        return "Mouse C"
