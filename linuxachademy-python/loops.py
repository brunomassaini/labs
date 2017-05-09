for number in range(1,11):
    if number % 2 > 0:
        print number

for number in range (1,10):
    if number == 5:
        print "I have counted to %s" % number
        break

for number in range (1,10):
    if number == 5:
        print "I have counted to %s" % number
    else:
        print "It's %s" % number + ", not 5"

string = "1 and 2 and 3"
for x in string:
    if x.isdigit():
        print x + " digit"


#########################
import random

heads_in_a_row_needed = 10
heads_in_a_row = 0
total_tries = 0

while heads_in_a_row_needed != heads_in_a_row:
    toss = random.randint(0,1)
    if toss == 1:
        heads_in_a_row += 1
    else:
        heads_in_a_row = 0
    total_tries += 1

print "It took %s tries to get %s heads in a row" % (total_tries, heads_in_a_row)