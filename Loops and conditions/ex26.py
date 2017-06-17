#41. Write a Python program to get next day of a given date

year = int(raw_input("Please enter a year: "))
month = int(raw_input("Please enter a month[1-12]: "))
day = int(raw_input("Please enter a year[1-31]: "))

date_list = []

import calendar

if month == 2 and day > 28 and not calendar.isleap(year):    
    print "sorry"
    exit()
elif month == 2 and day == 28 and calendar.isleap(year):    
    day += 1        
elif month == 2 and day == 29 and calendar.isleap(year):
    month +=1 
    day -= 28   
elif day == 31 and month == 12:
    year +=1
    day -= 30
    month -= 11
else:
    day += 1

date_list.append(str(year))
date_list.append(str(month))
date_list.append(str(day))

joined_elem = "-".join(date_list)

print joined_elem
