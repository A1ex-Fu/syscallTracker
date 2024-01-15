import sys
from collections import defaultdict
import csv

syscalls = defaultdict(str)

with open('syscalls.csv') as csvfile:
    for row in csv.reader(csvfile):
        syscalls[row[0]] = row[1]

d = defaultdict(int)



with open('test.txt') as readFile:
    lines = readFile.readlines()
    for line in lines:
        syscall_num = line.split("(")[0]
        d[syscall_num] += 1

with open(sys.argv[1],"a") as outputFile:
    for element in sorted(d.items(), key=lambda x:-x[1]):
        print(element)
        outputFile.writelines("%s (%s), used %d times\n" % (element[0], syscalls[element[0]], element[1]))