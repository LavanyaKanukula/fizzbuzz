#create the output file
output = open("C:\\Users\lavan\Python_Assignment_Midterm\\fizzbuzz-lavanya\File2.txt", 'w')
#fetch the input file
input = open("C:\\Users\lavan\Python_Assignment_Midterm\\fizzbuzz-lavanya\File1.txt")
lines = input.readlines()
#create a empty list
converted_text = []
for line in lines:
    line = line.replace("er","xor")
    line = line.replace("er","zor")
    line = line.replace("A","4")
    line = line.replace("a","4")
    line = line.replace("E","3")
    line = line.replace("e","3")
    line = line.replace("I","1")
    line = line.replace("i","1")
    line = line.replace("O","0")
    line = line.replace("o","0")
    converted_text.append(line) #this is a list
    
' '.join(converted_text) 
output.write(str(' '.join(converted_text)))

