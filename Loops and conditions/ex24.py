#38. Write a Python program to display astrological sign for given date of birth.

day_of_birth = int(raw_input("Please eneter day of your birth: "))
month_of_birth = raw_input("Please eneter month of your birth: ")

if day_of_birth > 21 and month_of_birth == "March" or day_of_birth > 20 and month_of_birth == "April":
    sign = "Aries"
elif day_of_birth < 21 and month_of_birth == "April" or day_of_birth < 21 and month_of_birth == "May":
    sign = "Taurus"
elif day_of_birth > 22 and month_of_birth == "May" or day_of_birth > 21 and month_of_birth == "June":
    sign = "Gemini"
elif day_of_birth < 22 and month_of_birth == "June" or day_of_birth < 22 and month_of_birth == "July":
    sign = "Cancer"
elif day_of_birth > 23 and month_of_birth == "July" or day_of_birth > 22 and month_of_birth == "August":
    sign = "Leo"
elif day_of_birth < 23 and month_of_birth == "August" or day_of_birth < 23 and month_of_birth == "September":
    sign = "Virgo"
elif day_of_birth > 24 and month_of_birth == "September" or day_of_birth > 23 and month_of_birth == "October":
    sign = "Libra"  
elif day_of_birth < 24 and month_of_birth == "October" or day_of_birth < 22 and month_of_birth == "November":
    sign = "Scorpio"
elif day_of_birth > 23 and month_of_birth == "November" or day_of_birth > 21 and month_of_birth == "December":
    sign = "Sagittarius"
elif day_of_birth < 22 and month_of_birth == "December" or day_of_birth < 20 and month_of_birth == "January":   
    sign = "Aquarius"
else:
    sign = "Pisces"    


print "Your sign is:", sign    