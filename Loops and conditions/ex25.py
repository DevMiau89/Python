#40. Write a Python program to find the median of three values.

num1 = int(raw_input("Please enter first number: "))
num2 = int(raw_input("Please enter a second number: "))
num3 = int(raw_input("Please enter a third number: "))

a_list = []
a_list.append(num1)
a_list.append(num2)
a_list.append(num3)

z = sorted(a_list)
print "Median of your number is:", z[1]




