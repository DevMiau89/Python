
#9. Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.
import re

def match_text(string):
    p = re.search(r'a.*b$', string, re.I | re.M ) 
    if p:
        print True
    else:
        print False

match_text("accddbbjjjb")

"dsadas*dsadas" -match "\*"