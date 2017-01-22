#!/usr/bin/python
# This script is used to count feedback-log record
import sys

count_pass = 0
count_fail = 0
count_invalid = 0
all_count = 0
for line in sys.stdin:
    list = line.split(",")
    if len(list) != 5:
        print list
        continue
    #print list
    if list[4] == "T\n":
        count_pass += 1
    else:
        if list[2] == "t:178":
            count_fail += 1
        else:
            if list[3].find("-") == -1:
                #print list, "is invalid"
                count_invalid += 1
            else:
                #print list, "is fail"
                count_fail += 1
    all_count += 1
    #if all_count % 10000000 == 0:
    #    print "count now:", all_count

print "count_pass:", count_pass
print "count_fail:", count_fail
print "count_invalid:", count_invalid
