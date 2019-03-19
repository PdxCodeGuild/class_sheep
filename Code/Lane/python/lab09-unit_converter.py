# unit converter Lab 9 version 1

#convert feet to meters
user_ft = float(input("What is the distance in feet?: "))
meters_in_feet = user_ft * .3048
print(f"{user_ft} ft is {meters_in_feet} m")


#version 2
#take user input for distance and units, convert to meters
unit_to_meter_dict = {'ft': 3.28, 'mi': 0.000621371, 'm': 1, 'km': .001}
while True:
    in_unit = input("What unit will you convert from? Use unit abbreviation: ")
    in_num = int(input("How many of these units?: "))
    out_unit = input("What unit do you want to convert to?: ")
    try:
        out_num = (in_num / unit_to_meter_dict[in_unit]) * unit_to_meter_dict[out_unit]
        print(f"There are {out_num} {in_unit}, in a {out_unit}.")
        break
    except KeyError:
        print("Bad units, try again!")


#version 3
#take user input for distance and units, convert to meters (supports additional units)
unit_to_meter_dict = {'mm': 1000, 'cm': 100, 'm': 1, 'km': .001, 'in':39.37, 'ft': 3.28, 'yd': 1.09, 'mi': 0.000621371, 'dm': 10}
while True:
    in_unit = input("What unit will you convert from? Use unit abbreviation: ")
    in_num = int(input("How many of these units?: "))
    out_unit = input("What unit do you want to convert to?: ")
    try:
        out_num = (in_num / unit_to_meter_dict[in_unit]) * unit_to_meter_dict[out_unit]
        print(f"There are {out_num} {in_unit}, in a {out_unit}.")
        break
    except KeyError:
        print("Bad units, try again!")
