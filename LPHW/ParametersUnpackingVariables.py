#from sys import argv

#script, first, second, third = argv

#print "The script is called:", script
#print "Your fisrt variable is:", first
#print "Your second variable is:", second
#print "Your third variable is:", third

# ARGV with user input together
from sys import argv

ScriptName, apple, pineapple, melon = argv
fourth = raw_input("What is your fourth variable? ")

print "The script is called: ", ScriptName
print "The second fruit is: ", apple
print "The third fruit is: ", pineapple
print "The last fruit is: ", melon

print "All together, your script is called %r, your first variable is %r, your second is %r, your third is %r, and your fourth is %r" % (ScriptName, apple, pineapple, melon, fourth)

#Mistake -> I skipped the argument assignement to the argv