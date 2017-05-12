line = "Oct 7 17:28:59 shirazk2141 sshd[2877]: Failed password for root from 31.220.3.180 port 50388 ssh2"

import re
match = re.search('^(.*?)\s(\w+)\ssshd.*?Failed\spass.*?from\s(.*?)\sport.*$', line)
print match
print match.groups()
print match.group(1)
print match.group(2)
print match.group(3)