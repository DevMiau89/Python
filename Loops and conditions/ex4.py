#4. Write a Python program to construct the following pattern, using a nested for loop.

for i in range(1,5):
    for j in range(0 + i):
        print "*",
    print ""   

for i in range(5,0,-1):
    tablica = []
    for j in range(i):
          tablica.append("*")
    print " ".join(tablica)      

print '================'

for i in range(5,0,-1):
    for j in range(i):
        print "*",
    print ""

for i in range(2,6):
    for j in range(0+i):
        print "*",
    print ""

#5. Write a Python program that accepts a word from the user and reverse it.
x = raw_input("Please enter your name:\n>>>")   

z = x[::-1]
print z

result = ""
for i in reversed(x):
    result += i

print result    

word = "chuj"
result_new = ""
for char in range(len(word) - 1, -1, -1):
    result_new += word[char]
print result_new

