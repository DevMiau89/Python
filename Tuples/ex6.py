#16. Write a Python program to convert a tuple to a dictionary.
my_tup = (1, 2, 3, 4, 5)


d = dict.fromkeys(my_tup,0)

print d
z = 1
for key in my_tup:    
    d[key] += z
    z += 1 
 
print d    

tuplex = (2, "w"),(3, "r")

print dict((x,y) for x,y in tuplex)

print tuplex