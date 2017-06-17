#10. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".

for i in range(51):
    if i % 3 == 0 and i % 5 == 0:
        print "fizzbuzz"
    elif i % 5 == 0:
        print "buzz"
    elif i % 3 == 0:
        print "fizz"
    else:
        print i


#11. Write a Python program which takes two digits m (row) and n (column) as input and generates a two-dimensional array. The element value in the i-th row and j-th column of the array should be i*j.        

columns = int(raw_input("Please enter the number of columns: "))
rows = int(raw_input("Please enter the number of rows: "))

table = [[0 for i in range(columns)] for j in range(rows)]

print table

s = []

for i in range(rows):
    s.append([])
    for j in range(columns):
        s[i].append(i*j)

print s       


