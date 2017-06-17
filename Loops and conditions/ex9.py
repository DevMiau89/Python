#13. Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and print the numbers that are divisible by 5 in a comma separated sequence. 

binary_input = raw_input("Please enter the 4 digit bianry numbers and separate them by comma: ")

z = binary_input.split(",")
print z 

for elem in z:
    conv_elem = int(elem, 2)
    if conv_elem % 5 == 0:
        print elem

#14. Write a Python program that accepts a string and calculate the number of digits and letters.

letters = 0 
digits = 0

sample_str = raw_input("Please enter a string: ")

for i in sample_str:
    if i.isalpha():
        letters += 1
    elif i.isdigit():
        digits += 1

print letters
print digits    

x = "kocikot123"

l = sum(letter.isalpha() for letter in x)
d = sum(letter.isdigit() for letter in x)

print l
print d

