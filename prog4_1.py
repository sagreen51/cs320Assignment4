import sys
import os

x = '#'
print("Assignment",x,end = '')
print("4-1, Steven Green, s.a.green51@gmail.com")
fileName = sys.argv[1]
'''fileName = fileName.strip()
print(fileName)'''
test_file = open(fileName,"r+")
text_in_file = test_file.readlines()
string = []

print("0",text_in_file)

for r in text_in_file:
    print(r.replace(" ", ","))







temp = " ".join(text_in_file)
print("1",temp,end="")

str_list = temp.split(" ");
print("2",str_list)

for s in str_list:
    if(s ==""):
        continue
    elif(s == '\n'):
        string += s
    else:
        string += s
        string += ","

print("".join(string))







