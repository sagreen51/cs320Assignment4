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
i=0
while (text_in_file[i] is not None):
	str = text_in_file[i]
	temp = str.split(" ")
	j=0
	while(temp[j] is not None):
		if (temp[j] == " "):
			print(",")
		else:
			print(temp[j])
		j+=1
	i+=1
'''for i in range(0,4):
	str = text_in_file[i]
	print(str.replace(" ",","),end = "")
print()'''
