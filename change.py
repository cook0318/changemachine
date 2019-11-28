# function that calculates total change needed.
def changeCounter():
    total = float(input("Please input total "))
    payment = float(input("Please input money tendered "))
    change = payment - total
    return change
# this function takes the change above, and begins breaking it down, largest denomination to smallest.
def changeMaker(change):
    toonie = change//2.0    
    change = change%2.0
    loonie = change//1.0
    change = change%1.0
    quarter = change//0.25
    change = change%0.25
    dime = change//0.10
    change = change%0.10
    nickle = change//0.05
    change = change%0.05
    penny = round((change*100),0) #had to round pennies because math was being wonky, giving numbers like 0.007000000000000032 
    return toonie, loonie, quarter, dime, nickle, penny

#this function keeps track of the total coins inside the machine.
def coinTotaler(toonieCount, loonieCount, quarterCount, dimeCount, nickleCount, pennyCount, toonie, loonie, quarter, dime, nickle, penny):
    toonieCount -= toonie
    loonieCount -= loonie
    quarterCount -= quarter 
    dimeCount -= dime
    nickleCount -= nickle
    pennyCount -= penny
    return toonieCount, loonieCount, quarterCount, dimeCount, nickleCount, pennyCount

def changeMachine():
    active = True
    toonieCount=100
    loonieCount=100
    quarterCount=100
    dimeCount=100
    nickleCount=100
    pennyCount=100
    while active: #keeps function running completely. can add in input statements for above totals, so users can input totals at beginning of day/upon start up
        if toonieCount <= 5 or loonieCount <= 5 or quarterCount <= 5 or dimeCount <= 5 or nickleCount <= 5 or pennyCount <= 5:
            print("Tender running low. Please add coins.") 
        userInput = input("What would you like to do? Calculate 'change', check coin 'total', or 'add' coins? ")
        if userInput == "change":
            change  = changeCounter()
            toonie, loonie, quarter, dime, nickle, penny = changeMaker(change)
            if toonie > toonieCount or loonie > loonieCount or quarter > quarterCount or dime > dimeCount or nickle > nickleCount or penny > pennyCount:
                print("Unable to fufill change. Please add coins.")    # if the machine needs more then it has, it does not take coins out of totals and instead prints an error.
            else:
                toonieCount, loonieCount, quarterCount, dimeCount, nickleCount, pennyCount = coinTotaler(toonieCount, loonieCount, quarterCount, dimeCount, nickleCount, pennyCount, toonie, loonie, quarter, dime, nickle, penny)
                print("Change needed: {} toonies, {} loonies, {} quarters, {} dimes, {} nickles, and {} pennies.".format (int(toonie), int(loonie), int(quarter), int(dime), int(nickle), int(penny)))
        elif userInput == "total":
            print("Coin totals: {} toonies, {} loonies, {} quarters, {} dimes, {} nickles, and {} pennies.".format(toonieCount, loonieCount, quarterCount, dimeCount, nickleCount, pennyCount))
        elif userInput == "add":
            print("Current coin totals: {} toonies, {} loonies, {} quarters, {} dimes, {} nickles, and {} pennies.".format(toonieCount, loonieCount, quarterCount, dimeCount, nickleCount, pennyCount))
            toonieCount += int(input("How many toonies have you added? "))
            loonieCount += int(input("How many loonies have you added? "))
            quarterCount += int(input("How many quarters have you added? "))
            dimeCount += int(input("How many dimes have you added? "))
            nickleCount += int(input("How many nickles have you added? "))
            pennyCount += int(input("How many pennies have you added? "))
            print("Your new coin totals are: {} toonies, {} loonies, {} quarters, {} dimes, {} nickles, and {} pennies.".format(toonieCount, loonieCount, quarterCount, dimeCount, nickleCount, pennyCount))
        else: 
            print("error")


changeMachine()


#possible additions: if machine runs out of toonies, use two loonies instead, or 4 quarters instead of loonies, etc.
#could add bills