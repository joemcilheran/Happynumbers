def summm(begin):
    posint = begin + 1
    posint = list(posint)
    squarelist = (int(digit)**2 for digit in posint)
    listsum = sum(squarelist)  
    if (int(listsum) == 1):
        print(posint)
    elif (int(listsum) == 4):
        
        
        
summm()
