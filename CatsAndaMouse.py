#CatsAndaMouse

def catAndMouse(x, y, z):
    diffAC = abs(z-x)
    diffBC = abs(z-y)
    
    if(diffAC == diffBC):
        return "Mouse C"
    elif(diffAC < diffBC):
        return "Cat A"
    else:
        return "Cat B"
