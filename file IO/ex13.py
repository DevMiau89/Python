#15. Write a Python program to read a random line from a file.
import random

with open("C:\case_test.txt", "r") as f:
    print random.choice(f.readlines())

print "---------------------"

def random_line(fname):  
    lines = open(fname).read().splitlines()  
    return random.choice(lines)  
print(random_line('C:\ex15_sample.txt'))      