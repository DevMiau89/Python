#6. Write a Python program to count the number of even and odd numbers from a series of numbers.
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

even_nums = 0
odd_nums = 0

for num in numbers:
    if num % 2 == 0:
        even_nums += 1
    else:
        odd_nums +=1

print "Number of enven number is: {0}".format(even_nums)
print "Number of odd number is: {0}".format(odd_nums)

#7. Write a Python program that prints each item and its corresponding type from the following list.

datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]

for i in datalist:
    print "Type of {0} is {1}".format(i, type(i))

print "================="

#8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.    

for i in range(0,6):
    if i == 3 or i==6:
        continue
    print i