def allNumbers():
    happyNumbers = []
    while len(happyNumbers) < 21:
        for posint in range(1,100):
            sumsquare(posint)
            happy = happyCheck(posint)
            if happy == True:
                happyNumbers.append(posint)  
            else:
                addtochecklist(happy) 
                check = addtochecklist(happy)
                if check == True:
                                    
    print(happyNumbers)
        
def sumsquare(positiveinteger):
    posintlist = [int(digit) for digit in str(positiveinteger)]
    squarelist = [int(digit)**2 for digit in posintlist]
    sumsquare = sum(squarelist)
    return sumsquare
    
def happyCheck(sumsquare):
    sumsquare = int(sumsquare)
    if sumsquare == 1:
       return True
    else:
       return sumsquare

def addtochecklist(item):
    checklist = []
    item = item
    if item not in checklist:
        checklist.append(item)
        True
    else:
        False
        
           

allNumbers()