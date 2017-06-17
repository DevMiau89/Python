#5. Write a Python program that matches a string that has an a followed by three 'b'.
import re
def text_match(string):
    p = re.match(r'ab{3}', string)
    if p:
        print True
    else:
        print False

text_match("abbb")

print "----------------------"

#6. Write a Python program that matches a string that has an a followed by two to three 'b'.
def match_text(string):
    p = re.match(r'ab{2,3}', string)
    if p:
        print True
    else:
        print False

match_text("abbbbbbbbbb")
