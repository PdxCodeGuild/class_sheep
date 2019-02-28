units = {
"mm": {"mm": 1, "cm": 0.1, "in": 0.039370079, "ft": 0.0032808399, "yd": 0.0010936133, "m": 0.001, "km": 0.000001},
"cm": {"mm": 10, "cm": 1, "in": 0.39370079, "ft": 0.032808399, "yd": 0.010936133, "m": 0.01, "km": 0.0001, "mi": 0.000006213712},
"in": {"mm": 25.4, "cm": 2.54, "in": 1, "ft": 0.083333333, "yd": 0.027777778, "m": 0.0254, "km": 0.0000254, "mi": 0.00001578282828283},
"ft": {"mm": 304.8, "cm": 30.48, "in": 12, "ft": 1, "yd": 1/3, "m": 0.3048, "km": 0.0003048, "mi": 0.0001893939393939},
"yd": {"mm": 914.4, "cm": 91.44, "in": 36, "ft": 3, "yd": 1, "m": 0.9144, "km": 0.0009144, "mi": 0.0005681818181818},
"m":  {"mm": 1000, "cm": 100,  "in": 39.37007874016, "ft": 3.280839895013, "yd": 1.093613298338, "m": 1, "km": 0.001, "mi": 0.0006213711922373},
"km": {"mm": 100000, "cm": 10000,  "in": 39370.07874016, "ft": 3280.839895013, "yd": 1093.613298338, "m": 1000, "km": 1, "mi": 0.6213711922373},
"mi": {"mm": 1609344, "cm": 160934.4,  "in": 63360, "ft": 5280, "yd": 1760, "m": 1609.344, "km": 1.609344, "mi":1}
}

def unitconvert(x,y,z):
    output = units[x][y]*z
    return output

while True:
    src = input("Which unit are you converting from?\n(mm/cm/in/ft/yd/m/km/mi)\n")
    if src not in units:
        print("Invalid unit.")
        continue
    else:
        break
amt = int(input(f"Enter value in {src}:\n"))
while True:
    dest = input("Which unit are you converting to?\n")
    if dest not in units:
        print("Invalid unit.")
        continue
    else:
        break

print(f"{amt} {src} = {unitconvert(src,dest,amt)} {dest}")
