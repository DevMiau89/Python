print "Please Enter your number: "
num = int(raw_input("> "))

alist = range(1, num + 1) 

userList = []

for i in alist:
    if num % i == 0:
        userList.append(i)

print userList        

# Mistake >>> I didn't add in range (num + 1) but declared my own scope