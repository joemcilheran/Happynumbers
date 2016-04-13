def allNumbers():
    happyNumbers = []
    for posint in range(1,10000):
        happy = happycheck(posint)
        if happy == True and len(happyNumbers) < 21:
            happyNumbers.append(posint)
        elif len(happyNumbers) >= 20:
            break
    print(happyNumbers)
    
def happycheck(number):
    seenNumbers = set()
    while number != 1:
        number = sum(int(digit)**2 for digit in str(number))
        if number in seenNumbers:
            return False
        seenNumbers.add(number)
    return True
            
        
allNumbers()
