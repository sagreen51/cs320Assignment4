import sys
import os
import StackMachine

x = '#'
print("Assignment",x,end = '')
print("4-1, Steven Green, s.a.green51@gmail.com")
fileName = sys.argv[1]
test_file = open(fileName,"r+")
text_in_file = test_file.readlines()

#print("0",text_in_file)

for r in text_in_file:
    print(r.replace(" ", ","),end = "")
    print(r)
