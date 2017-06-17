#1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).

new_list = []

for i in range(1500, 1700):
    if i % 7 == 0 and i % 5 == 0:
        new_list.append(str(i))


print ",".join(new_list)


#2. Write a Python program to convert temperatures to and from celsius, fahrenheit.

x = raw_input("would you like to convert fahrenheit(f) or celsius(c)?")

if x == "c":
    d = raw_input("how much would you like to convert?")
    z = (int(d) * 1.8) + 32
    print "{0} celsius is {1} farenheit".format(d, z)
else:
    k = raw_input("how much would you like to convert?")
    y = (int(k) - 32) / 1.8
    print "{0} celsius is {1} farenheit".format(k, y)


 

