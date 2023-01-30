import random
output = open("c:\\Users\lavan\Python_Assignment_Midterm\\fizzbuzz-lavanya\File2.txt", 'w')
    # Creating "File2.txt" as output
input = open("c:\\Users\lavan\Python_Assignment_Midterm\\fizzbuzz-lavanya\File1.txt")
lines = input.readlines()
converted_text = []
for line in lines:
        line = line.replace("ck", "x")
        line = line.replace("er", "or")
        line = line.replace("er", "or")
        line = line.replace("A", "4")
        line = line.replace("a", "4")
        line = line.replace("E", "3")
        line = line.replace("e", "3")
        line = line.replace("i", "1")
        line = line.replace("I", "1")
        line = line.replace("o", "0")
        line = line.replace("O", "0")
        converted_text.append(line) 
#print(str(''.join(converted_text)))   
''.join(converted_text)
output.write(str(''.join(converted_text)))