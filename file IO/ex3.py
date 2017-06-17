#3. Write a Python program to append text to a file and display the text.
foo = open("C:\case_test.txt", "r+") 
data = foo.write("Hello Python. I love you.\n")

print foo.read()

foo.close()