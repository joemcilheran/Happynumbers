def allNumbers():
    happyNumbers = []
    while len(happyNumbers) < 21:
        for posint in range(1,100):
            happy = happyCheck(posint,"")
            happyNumbers.append(happy)
    print(happyNumbers)
        
        
def happyCheck(positiveinteger,seenlist):
    seen = [seenlist] 
    posintlist = [int(digit) for digit in str(positiveinteger)]
    print(posintlist)
    squarelist = [int(digit)**2 for digit in posintlist]
    print(squarelist)
    sumsquare = sum(squarelist)
    print (sumsquare)
    if sumsquare == 1:
        print (positiveinteger)
        return positiveinteger
    elif str(sumsquare) in seen:
        False
    else:
        seen.append(sumsquare)
        happyCheck(sumsquare,"")
        print("ELSE")
        
            
           
#allNumbers()
#happyCheck(1, "")
happyCheck(7, "")
#happyCheck(10, "")

