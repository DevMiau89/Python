#46. Write a Python program to find all adverbs and their positions in a given sentence.
import re

sample_text = """
Clearly, he has no excuse for such behavior.
He was carefully disguised but captured quickly by police.
"""

pattern = r"\w+ly"

for a in re.finditer(pattern, sample_text):
    print "{0}-{1}: {2}".format(a.start(), a.end(), a.group(0))

print "-------------------------------"

#47. Write a Python program to split a string with multiple delimiters. 
text = 'The quick brown\nfox jumps*over the lazy dog.'

print re.split(r"\n|\*|;|,", text)

print "---------------------------------"

#48. Write a Python program to check a decimal with a precision of 2.
def is_decimal(num):
    import re
    pattern = re.match(r"\d+\.\d{2}$", num)
    if pattern:
        return True
    else:
        return False

print(is_decimal('123.11'))
print(is_decimal('123.1'))
print(is_decimal('123'))
print(is_decimal('0.21'))