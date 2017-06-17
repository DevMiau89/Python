#15. Write a Python program that accepts a hyphen-separated sequence of words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.

y = raw_input("Please enter the colors: ")
y=y.split(",")
y=sorted(y)
print "-".join(y)

items=[n for n in raw_input().split(',')]
items.sort()
print '-'.join(items)


