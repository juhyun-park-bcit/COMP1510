# a
pi = 3.14159
# b
radius = float(input("enter a radius value: "))
# c
surface_area = 4 * pi * radius**2
# d
print(f"this is the surface area: {surface_area}")
# e
volume = (4/3) * pi * radius**3
print(f"this is the volume: {volume}")
# f, g, h
double_radius = radius * 2
surface_area_with_double_radius = 4 * pi * double_radius**2
volume_double_radius = (4/3) * pi * double_radius**3
# i
print(f"The surface area with a doubled radius({double_radius}), is {surface_area_with_double_radius/surface_area} times as much as the surface area with a radius({radius}).")
print(f"The volume with a doubled radius({double_radius}), is {volume_double_radius/volume} times as much as the volume with a radius({radius}).")