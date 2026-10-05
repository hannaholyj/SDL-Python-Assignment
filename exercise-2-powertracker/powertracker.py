import random #need to randomly gen number and whether it will be squared or cubed

#defining function to square a number 
def squared(x):
    return x**2
def cubed(y):
    return y**3
#store all results 
results = []
iterations = 1 #first iteration = 1
while True:
    x = random.choice(range(1,21)) #random number between 1 and 20
    #randomly select cube or square (0=cube, 1=square)
    y = random.choice(range(2))
    #cube (y=0)
    if y == 0:
        result = cubed(x)
        print("Loop", iterations,":",x,"^3 =", result)
    elif y == 1:
        result = squared(x)
        print("Loop",iterations,":",x,"^2 = ", result)
    #storing all results 
    results.append(result)
    #comparing current result to last - if divisable - program ends 
    if iterations > 1 and last_res !=1: #can only compare after 2 iterations 
        if result % last_res == 0:
            print(result, "is divisable by", last_res)
            break #ends loop
    #replacing last_res with new result for next iteration 
    last_res = result 
    #add next iteration 
    iterations += 1 
#printing results 
print("The Largest Result is:", max(results))
print("The Smallest Result is:", min(results))
print("We Completed", iterations,"Loops")
        
    
    
   
    
   
   

    