try:
    print 1/0
except ZeroDivisionError:
    print "Cannot divide by a zero"
else:
    print "All good"