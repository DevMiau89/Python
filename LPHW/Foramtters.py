
#Difference between %s (is for display) and %r (debugging and raw representation)
import datetime
d = datetime.date.today()
print "Str = %s" % d
#'2011-05-14'
print "Repr = %r" % d
#'datetime.date(2011, 5, 14)'