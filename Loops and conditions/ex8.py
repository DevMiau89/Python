
#12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).

lines = []

while True:   
    z = raw_input("Please enter a sentence: ")
    if z:
        lines.append(z)
    else:
        break    

for i in lines:
    print i.upper()


