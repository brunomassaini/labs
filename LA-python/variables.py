STRING_VAR = "string-teste"
PHRASE = "    This is for testing yah"
NUMBER_VAR1 = 123
NUMBER_VAR2 = "123"

#1
print "1-----------------"
print STRING_VAR
#2
print "2-----------------"
print NUMBER_VAR1
#3
print "3-----------------"
print NUMBER_VAR2

### Math operations
#4
print "4-----------------"
print NUMBER_VAR1 + 1

### Forcing math operations with string numbers
### force the number type
#5
print "5-----------------"
print int(NUMBER_VAR2) + 1
### force the number type and decimals
#6
print "6-----------------"
print float(NUMBER_VAR2) + 1
#7
print "7-----------------"
print (float(NUMBER_VAR2) + 1) / NUMBER_VAR1
### spicify how many decimals
#8
print "8-----------------"
print round((float(NUMBER_VAR2) + 1) / NUMBER_VAR1, 4)
#9
print "9-----------------"
print type(NUMBER_VAR1)
#10
print "10-----------------"
print type(NUMBER_VAR2)

### working with strings
#11
print "11-----------------"
print "String value: %s" % STRING_VAR
#12
print "12-----------------"
print len(PHRASE)
#13
print "13-----------------"
print "-".join((STRING_VAR, NUMBER_VAR2))
#14
print "14-----------------"
print "teste" in STRING_VAR
#15
print "15-----------------"
print "dasdas" in STRING_VAR
#16
print "16-----------------"
print PHRASE.find("yah")
#17
print "17-----------------"
print PHRASE[0:16]
#18
print "18-----------------"
print PHRASE[16:23]
#19
print "19-----------------"
print PHRASE.strip()
