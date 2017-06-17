from sys import argv

script, user_name, user_age  = argv
prompt = "question "

print "\nHi %s, I'm the %s script" % (user_name,script)
print "\nOh, so you are %r years old. That's nice." % (user_age)
print "\nI'd like to ask you a few questions."
print "\nDo you like me %s " % user_name
likes = raw_input (prompt+'1: ')

print "\nWhere do you live %s ?" % user_name
lives = raw_input (prompt+'2: ')

print "\nWhat kind of computer do you have?"
computer = raw_input (prompt+'3: ')

print """\n
Alright, so you said %r about liking me.
And you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# I forgot about raw_input LOL:)