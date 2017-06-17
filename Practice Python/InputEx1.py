print "Please Enter your age: "
age = int(raw_input("> "))

print "Please Enter your name: "
name = raw_input("> ")

print "How many time would you like to print the message?"
message = int(raw_input("> "))

print "\nYou are {} years old and your name is {}. You will turn 100 years old".format(age, name)
print  "\nYour message will be printed %d times\n" % message

print (message * "\nYou are {} years old and your name is {}. You will turn 100 years old\n".format(age, name))

# String Play

str3 = "Hello Kot"
str1 = " Puszyk "
str2 = " kocha "

print (str(4) + " and" + str1)

print (str3 + " ktory kocha Puszyk")

print (str3 + str1 + str2)