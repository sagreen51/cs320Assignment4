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

str = " ".join(text_in_file)
str_list = str.split(" ");
i  =0
while (i < len(str_list)):
	str = str_list[i]
	if (str == ""):
		i +=1
	else:
		print(str,end = "")
		i +=1
		print(",",end = "")
'''for i in range(0,4):
	str = text_in_file[i]
	print(str.replace(" ",","),end = "")
print()'''
