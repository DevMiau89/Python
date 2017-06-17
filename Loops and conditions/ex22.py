#37. Write a Python program that reads two integers representing a month and day and prints the season for that month and day.

month = raw_input("Please enter a month: ")
day = int(raw_input("Please enter a day: "))

if (day > 21 and month == 'December') or (day <= 20 and month == 'March') or (month == "February") or (month == "January"):
    print "season is winter"
elif (day > 21 and month == "March") or (month == "April") or (day < 20 and month == "May"):
    print "season is spring"
elif (day >= 21 and month == "June") or (month == "July") or (day <= 20 and month == "August"):
    print "season is summer"
else:
    print "season is fall" 