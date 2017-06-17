#7. Write a Python program to find sequences of lowercase letters joined with a underscore. 
import re

def match_text(string):
    p = re.search(r'\_\w', string) #QUESTION
    if p:
        print True
    else:
        print False

match_text("t_b")
