list1 = [1,2,3,4]
list2 = range(1,19)

print list1
print list2
print list2[5]

###############
import os

partition_usage_treshold = 5
df_cmd = os.system("df -k")
lines = df_cmd.splitlines()

for line in lines[1:]:
    columns = line.split()
    used_percentage = columns[4]
    used_percentage = used_percentage.replace('%','')
    if int(used_percentage) >= partition_usage_treshold:
        print "partition %s usage is beyond threshold at %s" % (columns[0],columns[4])
