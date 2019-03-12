#lab20.py
#Credit Card Validation

#mynum.copy()
#mynum.index()

#tool to split strings into lists
def listconverter(instring):
    outlist = []
    for piece in instring:
        outlist.append(int(piece))
    return outlist

#tool to double every other index
def indexdoubler(inlist):
    for index in range(len(inlist)):
        if index % 2 == 0:
            inlist[index] = inlist[index]*2

#tool to subtract 9 from all indices with value > 9
def indexsubtractor(inlist):
    for index in range(len(inlist)):
        if inlist[index] > 9:
            inlist[index] = inlist[index] - 9

#tool to add all values of indices in a list together
def listadder(inlist):
    outsum = 0
    for index in range(len(inlist)):
        outsum += inlist[index]
    return outsum

#enter card number
cardstring = input("Please enter a card number. >")
# print(cardstring)
#turn cardstring into a list
cardlist = listconverter(cardstring)
# print(cardlist)
#split final check number from list and save in its own variable
checknum = cardlist.pop(len(cardlist)-1)
# print(checknum)
#reverse list
cardlist.reverse()
# print(cardlist)
#multiply every other index by 2
indexdoubler(cardlist)
# print(cardlist)
#subtract 9 from every index over 9
indexsubtractor(cardlist)
# print(cardlist)
#sum values in the list
cardsum = listadder(cardlist)
# print(cardsum)
#split out last digit of sum
sumlist = list(str(cardsum))
# print(sumlist)
compnum = sumlist[len(sumlist)-1]
compnum = int(compnum)
# print(compnum)
#check second digit against check number
if compnum == checknum:
    print(f"The card number {cardstring} is valid.")
else:
    print(f"The card number {cardstring} is not valid.")
