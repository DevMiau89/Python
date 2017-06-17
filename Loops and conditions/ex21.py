#36. Write a Python program to check a triangle is equilateral, isosceles or scalene.

side1 = int(raw_input("Please enter the length of side1: "))
side2 = int(raw_input("Please enter the length of side2: "))
side3 = int(raw_input("Please enter the length of side3: "))

if side1 == side2 == side3:
    print "equilateral triangle"
elif side1 != side2 != side3:
    print "scalene triangle"
else:
    print "isosceles triangle"  

          