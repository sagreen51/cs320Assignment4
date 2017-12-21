import sys
import os
import random

x = '#'
print("Assignment ",x,end = '')
print("4-1, Steven Green, s.a.green51@gmail.com")
fileName = str(sys.argv)
fileName = fileName.strip()
print(fileName)
test_file = open(fileName,"r+")
text_in_file = test_file.readlines()
print(text_in_file)
