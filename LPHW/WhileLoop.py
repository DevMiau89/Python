i = 0   # Variable declaration
j = 8
numbers = [] # declaration of an empty list

def while_loop_func(i, j): # Conversion to a function
    #i = 0
    #j = 8
    z = int(raw_input("Enter a number: "))
    while i < j:  # declaration of while loop
        print "At the top i is  %d" % i  # Here it will print the current i for me
        numbers.append(i) # Add number to a list using the append function

        i = i + z  # Add 1 to the current i number
        print "Numbers now", numbers # print the list with the added number
        print "At the bottom i is %d" % i # it will print i + 1

while_loop_func(0, 10)
print "The numbers: " # Here it will just print

for num in range(0,5): # starting for loop
    print num       # it will print all the numbers from numbers list
