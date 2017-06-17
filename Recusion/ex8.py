#11. Write a Python program to find  the greatest common divisor (gcd) of two integers.
def gdc(x, y):
    if y == 0:
        return x
    else:
        print "y is: ", y
        print "Modulo is:", x%y
        return gdc(y, x % y)

print gdc(24, 18)        


        