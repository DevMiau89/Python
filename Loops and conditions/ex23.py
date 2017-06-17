#38. Write a Python program to display astrological sign for given date of birth.

import collections

print "Find your Chinese Zodiac sign"
year_of_birth = int(raw_input("Please enter year of your birth: "))

animals = "Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"

animal_dict = collections.OrderedDict()

#print animals
#print animal_dict

iterator = 0
for i in range(1960, 2020):
    key = animals[iterator%12]
    if key in animal_dict:
        animal_dict[key].append(i)
    else:
        animal_dict[key] = [i]
    iterator += 1

#print animal_dict
z = list(k for k in animal_dict if year_of_birth in animal_dict[k])
print z

for key in animal_dict.keys():
    if year_of_birth in animal_dict[key]:
        print key
for animal in animals:
    if year_of_birth in animal_dict[animal]:
       print animal

