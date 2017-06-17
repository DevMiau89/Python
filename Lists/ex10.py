#43. Write a Python program to split a list into different variables.

a_list = [('love', 'yes', 'no'), ('valentine', 'no', 'yes'), ('day', 'yes','yes')]
var1, var2, var3 = a_list

print var1

#44. Write a Python program to generate groups of five consecutive numbers in a list


l = [[i + j for j in range(1,6)] for i in range(5)]

print l


for i in range(5):
    for j in range(1,6):
        print i + j


m = [i for i in range(0,10,2)]   

print m 

#45. Write a Python program to convert a pair of values into a sorted unique array
a_list = [(3,4),(1,2),(5,6)]

a_list.sort()

total = []

for i in a_list:
    total +=i

print total
    

