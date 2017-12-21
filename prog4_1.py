import sys
import os
import random

x = '#'
print("Assignment %c4-1, Steven Green, s.a.green51@gmail.com",x)
fileName = sys.stdin.readline()
'''fileName = fileName.strip()'''
print(fileName.name)
test_file = open(fileName,"r+")
text_in_file = test_file.readlines()
print(text_in_file)
