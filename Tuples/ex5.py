#13. Write a Python program to slice a tuple.
x = (1, 2, 3, 4, 5)

z = x[1:3]

print z

#14. Write a Python program to find the index of an item of a tuple.
tup = ('i', 'n', 'd', 'e', 'x', ' ', 't', 'u', 'p', 'l', 'e')

index = tup.index("i")
index1 = tup.index("e",2)
index2 = tup.index("d", 0,5)

print index
print index1
print index2

#15. Write a Python program to find the length of a tuple.
my_tup = (1, 2, 3, 4, 5)

lenght = len(my_tup)

print "---------------"
print lenght