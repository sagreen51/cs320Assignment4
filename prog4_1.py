import sys
import os
import random

x = '#'
print("Assignment",x,end = '')
print("4-1, Steven Green, s.a.green51@gmail.com")
fileName = sys.argv[1]
'''fileName = fileName.strip()
print(fileName)'''
test_file = open(fileName,"r+")
text_in_file = test_file.readlines()
i = 0
for i in range(0,4):
	str = text_in_file[i]
	",".join(str)
