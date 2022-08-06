num1 = 42 #variable declaration # number primitive data type 
num2 = 2.3 #variable declaration #number primitive data type
boolean = True #variable declaration #boolean data types 
string = 'Hello World' #variable declaration # string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration # dictionary 
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration #tuple
print(type(fruit)) # type check tuple
print(pizza_toppings[1]) # printing the pizza topping at index 1 being Sausage
pizza_toppings.append('Mushrooms') # add value to the end of an array 
print(person['name']) # printing the "name" of dictionary called "person"
person['name'] = 'George' # assigning a new value to "name" in dictionary 
person['eye_color'] = 'blue' # assigning a new value to "eye color" index in dictionary 
print(fruit[2]) # printing the fruit at index 3 from tuple "fruit" being banana 

if num1 > 45: # condition statement for a function checking in variable num1 is greater than 45
    print("It's greater") # priting a string only if it meets the 'if' condition
else: # condition statement for what to do if no previous conditions are met 
    print("It's lower") # printing a string only if 'else' condition is met 

if len(string) < 5: # condition statement to check if a string has a length of less than 5
    print("It's a short word!") # prints this string only if length of string in condition statement checks out 
elif len(string) > 15: # elif are condition statements that happen of the previous if statement conditions are not met 
    print("It's a long word!") # prints only if elif statement condition is met 
else: # condition statement for what to do if no previous conditions are met 
    print("Just right!") # printing a string only if 'else' condition is met 

for x in range(5): # for loop iterating through variable x in which the end of the range is 5
    print(x) #printing each iteration of value x 
for x in range(2,5): # for loop iterating through variable x in which the start of the range is 2, and ends at 5 
    print(x) #printing each iteration of value x 
for x in range(2,10,3): # for loop iterating through variable x in which the start of the range is 2, and ends at 10 and increments by 3 every loop
    print(x) #printing each iteration of value x 
x = 0 # variable x has a value of 0 
while(x < 5): # while loop that ranges the value at variable x to 5
    print(x)  #printing each iteration of value x 
    x += 1 # adding a count of one to the value of x 

pizza_toppings.pop() # removing the last string from the array 
pizza_toppings.pop(1) # removing the string from index 1 at the array 

print(person) # printing whole dictioanry to console 
person.pop('eye_color') # removing eye color item from dictionary person 
print(person) # printing the dictionary after the eye color has been removed

for topping in pizza_toppings: # for looop iterating through the toppings in pizza toppings array 
    if topping == 'Pepperoni': # conditional if statement requiring topping to on pepperoni string 
        continue # restarting code of block from the beginning 
    print('After 1st if statement') #printing a string 
    if topping == 'Olives' # conditional if statement requiring topping to be on olives string in order to execute
        break # if previous condition is met, completely stop the code and move onto next block of code 

def print_hello_ten_times(): # starting and naming a function.
    for num in range(10): # for loop iterating through the numbers 0 - 10 
        print('Hello') # prints hello 10 times from each iteration 

print_hello_ten_times() # calling the above function to print to console and execute 

def print_hello_x_times(x): # starting and naming a function and giving it a parameter of x 
    for num in range(x): # for loop that will iterate through num to whatever the value of the function parameter is 
        print('Hello') # printing hello for every iteration of the for loop 

print_hello_x_times(4) # calling the function and printing hello 4 times 

def print_hello_x_or_ten_times(x = 10): # starting and naming a new function with parameter of x = 10 
    for num in range(x): # for loop that will iterate through num to whatever the value of the function parameter is 
        print('Hello') # printing hello however many times the for loop iterates

print_hello_x_or_ten_times() # calling the function to print 10 times based of the parameter value 
print_hello_x_or_ten_times(4) # calling function and reaassigning value to parameter 


"""
Bonus section
"""

# print(num3)    # printing variable num3 
# num3 = 72        # reassigning new value to variable num3
# fruit[0] = 'cranberry'        # reassigning value to fruit at index 0 
# print(person['favorite_team'])     # printing the value at favorite team from dictionary perso n
# print(pizza_toppings[7])       # printing the pizza topping at index 7 
#   print(boolean)            # printing a if true or false 
# fruit.append('raspberry')    # adding string raspberry to tuple of fruits 
# fruit.pop(1)        # removing string from fruit tuple at index 1 
#  