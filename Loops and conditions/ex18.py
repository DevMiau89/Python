#31. Write a Python program to calculate a dog's age in dog's years.

human_years = int(raw_input("Please enter the dog's age: "))

if human_years <= 0:
    print "Age must be positive number"
    exit()
elif human_years <= 2:
    dog_years = human_years * 10.5
else:
    dog_years = (human_years - 2) * 4 + 21

print "The dog's age in dog's years is: {0}". format(dog_years)

#32. Write a Python program to check whether an alphabet is a vowel or consonant. 

letter = raw_input("Please enter the letter: ")
vowels = ('a','e','i','o','u','A','E','I','O','U')

if letter.startswith(vowels):
    print "letter is vowel"
elif letter == 'y':
	print("Sometimes letter y stand for vowel, sometimes stand for consonant.")
else:
    print "letter is consonant"

