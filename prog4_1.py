import sys
import os
import random


print("Assignment %#4-1, Steven Green, s.a.green51@gmail.com")
fileName = sys.stdin.readline()
fileName = fileName.strip()
print("%s".format(fileName))
test_file = open("testfile.txt","r+")
test_in_file = test_file.readlines()
print(test_in_file,end = "")
