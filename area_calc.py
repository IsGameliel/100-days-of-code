#write your code bellow this line
import math

def paint_calc(height, width, cover):
    cans = (height * width) / cover
    number_of_cans = math.ceil(cans)
    print(f"you will need {number_of_cans} cans of paint")


#write your code above this line 

# dont change the code below
test_h = int(input("Hight of wall: "))
test_w = int(input("width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)