#forloop

#instructions
'''Write a for loop that iterates over all elements of the areas
list and prints out every element separately.'''

#areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for element in areas:
    print(element)
    
    
#instructions
'''Adapt the for loop in the sample code to use enumerate() and use two iterator variables.
Update the print() statement so that on each run, a line of the form "room x: y" should be printed,
where x is the index of the list element and y is the actual list element, i.e. the area. Make sure
to print out this exact string, with the correct spacing.'''

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, element in enumerate(areas) :
    print("room " + str(index) + ": " + str(element))




#instructions

'''Adapt the print() function in the for loop so that the first printout becomes 
"room 1: 11.25", the second one "room 2: 18.0" and so on.'''

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for index, area in enumerate(areas) :
    print("room " + str(index + 1) + ": " + str(area))
    
    
#instructions
'''Write a for loop that goes through each sublist of house and prints out the x is y sqm, 
where x is the name of the room and y is the area of the room.'''

# house list of lists
house = [["hallway", 11.25], 
         ["kitchen", 18.0], 
         ["living room", 20.0], 
         ["bedroom", 10.75], 
         ["bathroom", 9.50]]
         
# Build a for loop from scratch
for each in house:
    room_name = each[0]
    room_area = each[1]
    print("the " + room_name + " is " + str(room_area) + " sqm")
    
    
#instructions
'''Write a for loop that goes through each key:value pair of europe. 
On each iteration, "the capital of x is y" should be printed out, 
where x is the key and y is the value of the pair.'''

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }
          
# Iterate over europe
for key, value in europe.items():
    print("the capital of " + key + " is " + value)
    
    
#instructions
'''Import the numpy package under the local alias np.
Write a for loop that iterates over all elements in np_height
and prints out "x inches" for each element, where x is the value in the array.
Write a for loop that visits every element of the np_baseball array and prints it out.'''

# Import numpy as np
import numpy as np

# For loop over np_height
for elements in np_height:
    print(str(elements) + " inches")


# For loop over np_baseball
for elements in np.nditer(np_baseball):
    print(elements)
    
    
#instructions
'''Write a for loop that iterates over the rows of cars and on each 
iteration perform two print() calls: one to print out the row label
and one to print out all of the rows contents.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows():
    print(lab)
    print(row)
    
    
#instructions
'''Using the iterators lab and row, adapt the code in the for loop such that
the first iteration prints out "US: 809", the second iteration "AUS: 731", and so on.
The output should be in the form "country: cars_per_cap". Make sure to print out this
exact string (with the correct spacing).You can use str() to convert your integer data 
to a string so that you can print it in conjunction with the country label.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))
    
    
    
#instructions
'''Use a for loop to add a new column, named COUNTRY, that contains a uppercase version
of the country names in the "country" column. You can use the string method upper() for this.
To see if your code worked, print out cars. Don't indent this code, so that it's not part of the for loop.'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Code for loop that adds COUNTRY column
for lab, row in cars.iterrows():
    cars.loc[lab, "COUNTRY"] = row["country"].upper()

# Print cars
print(cars)


#instructions
'''Replace the for loop with a one-liner that uses .apply(str.upper). 
The call should give the same result: a column COUNTRY should be added to cars,
containing an uppercase version of the country names.
As usual, print out cars to see the fruits of your hard labor'''

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Use .apply(str.upper)
for lab, row in cars.iterrows() :
    cars.loc[lab, "COUNTRY"] = row["country"]

cars["COUNTRY"] = cars["country"].apply(str.upper)