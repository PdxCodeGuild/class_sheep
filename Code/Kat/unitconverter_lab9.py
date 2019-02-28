# version 1
# in_feet = int(input("What is the distance in feet? >"))
# in_meters = in_feet * 0.3048
# print(f"The distance is {in_meters} meters.")

# version 2
print("Welcome to the distance converter!" + "\n")
# while user_dist not in unit_dict.keys():
#     user_dist = input("what is the distance in ft, mi, m, or km? >")
# def convert_meters(distance, meters):
#     if units == 'm':
#         return distance
#     elif units == "ft":
#         return distance * 0.3048
#     elif units == "mi":
#         return distance * 1609.34
#     elif units == "km":
#         return distance * 1000

# user_dist = input("How many units would you like to convert?")
# user_dist = float(int(user_dist))
# user_unit = input("Would you like to convert km, mi, m, or ft?")
# def conversion (user_dist, user_unit, unit_conversion):
#     return user_dist*convert_meters[user_unit]/convert_meters[unit_conversion]


meter_dict = {'ft': 0.3048, 'm': 1, 'mi': 1609.34, 'km': 1000}
chosen_unit = input("Choose input unit, ft, mi, m, or km?")
while chosen_unit not in meter_dict.keys():
    chosen_unit = input("what is the distance in ft, mi, m, or km? >")
in_num = int(input("How many?"))
print(f"That is {in_num * meter_dict[chosen_unit]} meters.")
# if chosen_unit == 'ft':
#     print(f"That is {in_num * meter_dict[chosen_unit]} meters.")
# elif chosen_unit == 'm':
#     print(f"That is {in_num * meter_dict[chosen_unit]} meters.")
# elif chosen_unit == 'mi':
#     print(f"That is {in_num * meter_dict[chosen_unit]} meters.")
# elif chosen_unit == 'km':
#     print(f"That is {in_num * meter_dict[chosen_unit]} meters.")
