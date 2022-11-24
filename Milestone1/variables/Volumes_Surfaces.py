
import math
#Cuboid
h=25/7
w=25/2
l=35
#Cone
h=10
r=3
Cuboid_Volume = l * w * h
print(Cuboid_Volume)
Cuboid_Surface_Area = 2*(l*w + l*h +h*w)
print(Cuboid_Surface_Area)
Cone_Volume = (math.pi) * r**2 * h/3
print(Cone_Volume)
Cone_Surface_area = (math.pi)*r*(r+math.sqrt(h**2 + r**2)) 
print(Cone_Surface_area)

print(f'The volume of Cuboid is {round(Cuboid_Volume,2)} and the surface area is {round(Cuboid_Surface_Area,2)}')
print(f'The volume of Cone is {round(Cone_Volume,2)} and the surface area is {round(Cone_Surface_area,2)}')




# %%
