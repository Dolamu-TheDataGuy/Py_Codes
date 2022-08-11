import math

def paint_calc(height, width, cover):
    area = height * width
    num_can = area / cover
    #num_can = round(num_can, 0)
    num_can = math.ceil(num_can)
    print(f"You will need {num_can} cans of paint")



test_h = int(input("Height of the wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height = test_h, width = test_w, cover = coverage)
