#4. Write a Python program to unpack a tuple in several variables.
julia = ("Julia", "Roberts", 1967, "Actress")

var1,var2,var3,var4 = julia

print (var1 + "," + "," + var2 + "," + str(var3) + "," + var4)

#5. Write a Python program to add an item in a tuple.

my_tuple = (1, "karolina", [1,2,"1989"])

f = 3.2,

z = my_tuple + f

print z

my_tuple = my_tuple[:2] + ("A",)  + f
print "-------------"

print my_tuple

#6. Write a Python program to convert a tuple to a string.

julia = ("Julia", "Roberts", 1967, "Actress")

s = str(julia)

print type(s)
print s

tup = ('e', 'x', 'e', 'r', 'c', 'i', 's', 'e', 's') 

z = "".join(tup)

print str(z)