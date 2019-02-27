#lab9
#Unit Converter
unit_dict = {'ft': 0.3048, 'm': 1, 'mi': 1609.34, 'km': 1000, 'yd': 0.9144, 'in': 0.0254}
inunit = input("What unit will you convert? >")
outunit = input("What unit do you want to convert it to? >")
distance = input("What is the total distance to convert? >")
distance = int(distance)
roundquery = input("Do you want to round the result? y/n. >")
metertotal = distance * unit_dict[inunit]
outtotal = metertotal / unit_dict[outunit]
if roundquery.lower() == 'y':
    roundtotal = round(outtotal)
    print(f"{distance}{inunit} is equal to {roundtotal}{outunit}.")
else:
    print(f"{distance}{inunit} is equal to {outtotal}{outunit}.")
