import math;


# wall_h= int (input("Type Wall height: "))
# wall_w= int (input("Type the wall width: "))
# surface_per_can= int(input("Type how many square meters it's possible to paint with 1 can?: "))

# number_of_cans =math.ceil((wall_h * wall_w) / surface_per_can)

# print(f"You'll need {number_of_cans} of paint")

def paint_calc(height, width, cover):
  area=height*width
  num_of_cans= math.ceil(area/cover)
  print(f"You'll need {num_of_cans} cans of paint")
  

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)





