import sys
import os
import random


print("Assignment 4-1, Steven Green, s.a.green51@gmail.com")
fileName = sys.stdin.readline()
fileName = fileName.strip()
print(fileName)
test_file = open(fileName,"r+")
test_in_file = test_file.readlines()
print(test_in_file,end = "")
