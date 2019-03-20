# truck_spill_finder.py
# Hint for lab 18 version 4
'''
You are controlling a satelite which can observe highway road, and see the
reflectiveness of the road. Sometimes you will be given an area where a truck
crashed and spilled a fluid. You will have to look to see how far the fluid
extends.

The road has reflectiveness of 2 or 3
'''
oil_spill_road = [2, 3, 2, 7, 7, 7, 7, 7, 7, 2, 2, 3, 2, 2, 5]
oil_spill_crash_location = 3
milk_spill_road = [2, 10, 10, 10, 10, 10, 10, 10, 10, 10, 3, 2, 2, 7, 2, 3]
milk_spill_crash_location = 1

def find_spill_location(road_spill, crash_location):
    spill_spot = road_spill[crash_location]
    viewpoint  = crash_location
    while True:
        viewpoint += 1
        if road_spill[viewpoint] != spill_spot:
            break
    return [crash_location, viewpoint - 1]

milk_spill_list = find_spill_location(milk_spill_road, milk_spill_crash_location)
print(f"The spill starts at {milk_spill_list[0]} and ends at {milk_spill_list[1]}")

'''
oil_spill_spot = oil_spill_road[oil_spill_crash_location]
# get all the sevens
viewpoint = oil_spill_crash_location
while True:
    viewpoint += 1
    if oil_spill_road[viewpoint] != oil_spill_spot:
        break
print(viewpoint)
print(f"The spill starts at {oil_spill_crash_location}, and ends at {viewpoint - 1}")
'''