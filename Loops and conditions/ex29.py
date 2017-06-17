#43. Write a Python program to create the multiplication table (from 1 to 10) of a number.

user_number = int(raw_input("Please enter a number: "))

number = 1

while number <= 10:
    result = user_number * number
    print user_number, '*', number, "=",result
    number +=1

#44. Write a Python program to construct the following pattern, using a nested loop number.

for i in range(1,10):
    for j in range (0 + i):
        print i,
    print ""    
    
for i in range(10):
    print(str(i) * i)