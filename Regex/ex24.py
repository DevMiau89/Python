#33. Write a Python program to find all five characters long word in a string.
import re

my_string = 'Pytho Exercises, PHPis exercises.'
pattern = re.findall(r'\b\w{5}\b', my_string)

print pattern

#34. Write a Python program to find all three, four, five characters long words in a string.
text = 'Pytho Exercises and PHPI exercises.'

pattern = re.findall(r'\b\w{3,5}\b', text)

print pattern

#35. Write a Python program to find all words which are at least 4 characters long in a string.
text1 = 'Pytho Exercises and PHPI exercises.'

pattern1 = re.findall(r'\b\w{4,}\b', text)

print pattern1