# Lab 9: Unit Converter
# This lab will involve writing a program that allows the user to convert a number between units.

print('Welcome to the distance converter!' + '\n')

# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

in_feet = int(input('What is the distance in feet? >'))
in_meters = in_feet * 0.3048
print(f'The distance is {in_meters} meters.')


# Version 2
# Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.
# 1 ft is 0.3048 m, 1 mi is 1609.34 m, 1 m is 1 m, 1 km is 1000 m
meter_dict = {'ft': 0.3048, 'm': 1, 'mi': 1609.34, 'km': 1000}
chosen_unit = input('Would you like to convert ft, mi, m, or km?')
while chosen_unit not in meter_dict:
    chosen_unit = input('what is the distance in ft, mi, m, or km? >')
in_num = int(input('How many?'))
print(f'That is {in_num * meter_dict[chosen_unit]} meters.')

#Version 3
# Add support for yards, and inches: 1 yard is 0.9144 m, 1 inch is 0.0254 m

# function to convert to meter
def convert_to_meters(input):
    if user_in_unit == 'm':
        return user_dist
    elif user_in_unit == 'ft':
        return user_dist * 0.3048
    elif user_in_unit == 'mi':
        return user_dist * 1609.34
    elif user_in_unit == 'km':
        return user_dist * 1000
    elif user_in_unit == 'in':
        return user_dist * 0.0254
    elif user_in_unit == 'yd':
        return user_dist * 0.9144

user_dist = float(input('How many units would you like to convert? > '))
user_in_unit = input('Would you like to convert km, mi, m, yd, in, or ft? > ')
print(f'{user_dist} {user_in_unit} is {convert_to_meters(user_dist)} meters.')


# Version 4
# Now we'll ask the user for the distance, the starting units, and the units to convert to.
# You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

user_dist = float(input('How many units would you like to convert? > '))
user_in_unit = input('What unit are you converting from: km, mi, m, yd, in, or ft? > ')
user_out_unit = input('What unit are you converting to: km, mi, m, yd, in, or ft? > ')

distance_in_meters = convert_to_meters(user_dist)

#function to convert from meters into other units
def convert_from_meters(distance_in_meters):
    if user_out_unit == 'm':
        return distance_in_meters
    elif user_out_unit == 'ft':
        return distance_in_meters / 0.3048
    elif user_out_unit == 'mi':
        return distance_in_meters / 1609.34
    elif user_out_unit == 'km':
        return distance_in_meters / 1000
    elif user_out_unit == 'in':
        return distance_in_meters / 0.0254
    elif user_out_unit == 'yd':
        return distance_in_meters / 0.9144

print(f'{user_dist} {user_in_unit} is {convert_from_meters(distance_in_meters)} {user_out_unit}.')
