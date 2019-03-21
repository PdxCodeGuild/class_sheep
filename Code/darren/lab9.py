#lab9
#Unit Converter
unit_dict = {'ft': 0.3048, 'm': 1, 'mi': 1609.34, 'km': 1000, 'yd': 0.9144, 'in': 0.0254}
in_unit = input("What unit will you convert? >")
while in_unit not in unit_dict:
    in_unit = input("What unit will you convert? >")
out_unit = input("What unit do you want to convert it to? >")
while out_unit not in unit_dict:
    out_unit = input("What unit do you want to convert it to? >")
distance = input("What is the total distance to convert? >")
round_query = input("Do you want to round the result? y/n. >")
out_total = (int(distance) * unit_dict[in_unit]) / unit_dict[out_unit]
if round_query.lower() == 'y':
    round_total = round(out_total)
    print(f"{distance} {in_unit} is equal to {round_total} {out_unit}.")
else:
    print(f"{distance} {in_unit} is equal to {out_total} {out_unit}.")

# meter_total = distance * unit_dict[in_unit]
# out_total = meter_total / unit_dict[out_unit]
