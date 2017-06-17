#33. Write a Python program to convert month name to a number of days.

months_30 = ["April", "June","September","November"]

months_31 = ["January","March","May","July", "August"
,"October","December"]

feb = "February"

users_month = raw_input("Please enter the month: ")

if users_month == feb:
    print "No. of days is: 28/29 days"
elif users_month in months_31:
    print "No. of days is: 31 days"
elif users_month in months_30:
    print "No. of days is: 30 days"
else:
    print "Wrong month"    



    