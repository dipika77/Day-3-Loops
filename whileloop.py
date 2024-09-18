#While Loop

#instructions
'''Create the variable offset with an initial value of 8.
Code a while loop that keeps running as long as offset is not equal to 0. Inside the while loop:
Print out the sentence "correcting...".
Next, decrease the value of offset by 1. You can do this with offset = offset - 1.
Finally, still within your loop, print out offset so you can see how it changes.'''

# Initialize offset
offset = 8

# Code the while loop
while offset != 0:
    print("correcting...")
    offset = offset - 1
    print(offset)
    
    
#instructions
'''Inside the while loop, complete the if-else statement:
If offset is greater than zero, you should decrease offset by 1.
Else, you should increase offset by 1.
If you've coded things correctly, hitting Submit Answer should work this time.'''

# Initialize offset
offset = -6

# Code the while loop
while offset != 0 :
    print("correcting...")
    if offset > 0 :
      offset-= 1
    else : 
      offset +=1  
    print(offset)
    
    

