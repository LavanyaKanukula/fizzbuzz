n = 100
i = 1
for i in range(1, n+1):
    #not multiples of 3 and 5
    if(i%3 != 0 and i%5 != 0): 
     print(i)
    # multiple of 3 and 5
    elif(i%3 == 0 and i%5 == 0): 
     print("FizzBuzz") 
     #multiples of 3
    elif(i%3 ==0):
     print("Fizz")
     #multiples 5
    else:
     if(i%5 == 0):
      print("Buzz")
    
    
      