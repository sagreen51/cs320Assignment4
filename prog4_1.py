import sys
import os
import random


print("Assignment %#4-1, Steven Green, s.a.green51@gmail.com")
fileName = sys.stdin.readline()
print(fileName)
test_file = open(fileName,"r+")
test_in_file = test_file.read()
print(test_in_file)
