#1. Write a Python program to create a tuple. 

my_list = []

for i in range(1,6):
    my_list.append(i)

print my_list   

tup = tuple(my_list)

print "--------------"
print tup

x = ()
print x

tuplex = tuple()
print tuplex

#2. Write a Python program to create a tuple with different data types. 

my_tuple = (1, "karolina", [1,2,"1989"], 3.2)

print my_tuple

#3. Write a Python program to create a tuple with numbers and print one item. 
num_tup = (1, 2, 3, 4, 5)

print num_tup[1]

num_tup = 1,

print num_tup