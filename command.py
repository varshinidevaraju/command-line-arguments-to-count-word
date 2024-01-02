#Developed by: VARSHINI D
 #Register number: 212223230234
 
import sys
count= 0
with open(sys.argv[1],'r') as file:
    for line in file:
        word= line.split()
        count += len(word)
print("Program developed by:varshini")
print("word count in file = ",count)