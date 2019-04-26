#Unit_converter


from decimal import *
getcontext().prec = 6

chosen_unit = input("choose (ft) of (in) of (m)>")
in_number = int(input('How many?'))
if chosen_unit == 'ft':
    print(f"That is {in_num / 3.2808} meters> ")
if chosen_unit =='in':
    print(f"That is {in_num / 39.37} meters> ")
if chosen_unit == 'm':
    print(f"That is {in_num / 1} meters> ")

# distance_feet = int(input("what is the distance in feet?"))
# distance_meters = Decimal(distance_feet) * Decimal(0.3048)
# print(f"{distance_feet}ft is {distance_meters}m")

meter_converter_dict = {'ft': 0.3048 ,'mi': 1609.34, 'm': 1, 'km':1000, 'yd':0.9144, 'in':0.0254}
km_converter_dict = {'ft': 0.0003048 ,'mi': 1.60934, 'm': 1000, 'km':1, 'yd':0.0009144, 'in':0.0000254}
ft_converter_dict = {'ft': 1 ,'mi': 1/5280, 'm': 3.28, 'km':3280.8, 'yd':0.333, 'in':12}
mi_converter_dict = {'ft': 5280 ,'mi': 1, 'm': 1609.34, 'km':1.60934, 'yd':1760, 'in':63360}

distance = int(input("what is the distance?> "))
input_unit = input("what are the input units?> ")
while input_unit not in meter_converter_dict.keys:
    input_unit = input("what are the units? choose 'ft', 'mi', 'm', or 'km'> ")
output_unit = input("what are the output units?> ")
while output_unit not in meter_converter_dict.keys:
    output_unit = input("what are the units? choose 'ft', 'mi', 'm', or 'km'> ")
converted_distance = (Decimal(distance) * Decimal(meter_converter_dict[input_unit]))/(Decimal(meter_converter_dict[output_unit]))

print(f"{distance}{input_unit} is equal to {converted_distance} {output_unit}")
