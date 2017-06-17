#49. Write a Python program to remove words from a string of length between 1 and a given number
import re

str1 = "The quick brown fox jumps over the lazy dog."
pattern = re.sub(r"\b\w{1,3}\b", "", str1) 
print pattern

#50. Write a Python program to remove the parenthesis area in a string
sample_data = ["example (.com)", "w3resource(.com)", "github (.com)", "stackoverflow (.com)"]

for i in sample_data:
    print re.sub(r"\(\.com\)+","", i)
    