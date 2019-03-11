#lab19.py
#Blackjack Advice

carddict = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
Acarddict = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}

def cardcalculator(inlist):
    cardtotal = 0
    for card in range(len(inlist)):
        cardtype = inlist[card]
        cardtotal +=  carddict[cardtype]
    return cardtotal

def acecalculator(inlist):
    cardtotal = 0
    for card in range(len(inlist)):
        cardtype = inlist[card]
        cardtotal +=  Acarddict[cardtype]
    return cardtotal

def advisor(innum):
    if innum > 21:
        advice = 'Already Busted'
    else:
        if innum < 17:
            advice = "You should hit!"
        if innum >= 17 and innum < 21:
            advice = "Stay."
        if innum == 21:
            advice = "Blackjack!"
    return advice

userhand=[]
for card in range(0,3):
    usercard = input("Please pick a card, up to three.> ")
    userhand.append(usercard)
print(userhand)
total = cardcalculator(userhand)
acetotal = 0
if total > 21:
    for num in range(len(userhand)):
        if userhand[num] == 'A':
            acetotal += 1
if acetotal > 1 and total > 21:
    total = acecalculator(userhand)
print(f"You have {total} points in your hand.")
tellme = advisor(total)
print(tellme)
