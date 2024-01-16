# b
coverage = 40
# c, d, e, f
length_meters = float(input("length of the room in meters: "))
width_meters = float(input("width of the room in meters: "))
height_meters = float(input("height of the room in meters: "))
coats = int(input("the number of coats: "))
# g, h, i
surface_area = (length_meters*width_meters) + 2*(length_meters*height_meters) + 2*(width_meters*height_meters)
total_coverage_needed = coats*surface_area
cans_of_paint_required = total_coverage_needed / coverage
# j
the_number_of_cans = -int(-(cans_of_paint_required) // 1)

print(f"How many cans of paint they need to buy? {the_number_of_cans}")