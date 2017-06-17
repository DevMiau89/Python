#ex38 Write a Python program to count occurrences of a substring in a string.
#ex39 Write a Python program to reverse a string.
#ex40 Write a Python program to reverse words in a string.
#ex41 Write a Python program to strip a set of characters from a string.

def occurances_count(word):
    dict = {}
    for letter in word:
        keys = dict.keys()
        if letter in keys:
            dict[letter] += 1
        else:
            dict[letter] = 1
    return dict        

print occurances_count("kot is nice and warm")

str1 = 'The quick brown fox jumps over the lazy dog.'  
print(str1.count("jumps"))

def reversed_words(sentence):
    return ''.join(reversed(sentence))

print reversed_words('The quick brown fox jumps over the lazy dog.')    

def reversed_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())
print('\n')
print reversed_words('The quick brown fox jumps over the lazy dog.')  


seq = '888The quick brown fox jumps over the lazy dog.88888888'
new_seq = seq.strip('8')

print new_seq

def characters_strip(seq, chars):
    return ''.join(c for c in seq if c not in chars)


print characters_strip('The quick brown fox jumps over the lazy dog.', 'a')

#ex42 Write a python program to count repeated characters in a string

import collections
the_string = 'thequickbrownfoxjumpsoverthelazydog'
results = collections.Counter(the_string)
print(results)

import collections  
str1 = 'thequickbrownfoxjumpsoverthelazydog'  
d = collections.defaultdict(int)  
for c in str1:  
    d[c] += 1  
      
for c in sorted(d, key=d.get, reverse=True):  
    if d[c] > 1:  
        print('%s %d' % (c, d[c]))  

  