num1 = 42 # variable declaration, numbers
num2 = 2.3 # variable declaration, numbers
boolean = True # variable declaration , boolean
string = 'Hello World' # variable declaration, string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, array
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, list?
print(type(fruit)) # log statement
print(pizza_toppings[1]) # log statement
pizza_toppings.append('Mushrooms') # append to array
print(person['name']) # log statement
person['name'] = 'George' # change dictionary name to George
person['eye_color'] = 'blue' # change dictionary eye_color to blue
print(fruit[2]) # log statement

if num1 > 45: # if statement
    print("It's greater") #log statement
else: # else statement
    print("It's lower") #log statement

if len(string) < 5: # if statement
    print("It's a short word!") #log statement
elif len(string) > 15: # else if statement
    print("It's a long word!") #log statement
else: # else statement
    print("Just right!")  #log statement

for x in range(5): # for loop
    print(x) #log statement
for x in range(2,5): # for loop
    print(x) #log statement
for x in range(2,10,3): # for loop
    print(x) #log statement
x = 0 # variable declaration
while(x < 5): # while loop
    print(x) #log statement
    x += 1 # while loop argument

pizza_toppings.pop() # remove last postion from pizza_topping array
pizza_toppings.pop(1) # remove position 1 from pizza_topping array

print(person) #log statement
person.pop('eye_color') # remove eye_color from dictionary
print(person) #log statement

for topping in pizza_toppings: # for loop
    if topping == 'Pepperoni': # if statement
        continue # continue statement
    print('After 1st if statement') # log statement
    if topping == 'Olives': # if statement
        break # break from for loop

def print_hello_ten_times(): # define function
    for num in range(10): # for statement
        print('Hello') #log statement

print_hello_ten_times() # call function

def print_hello_x_times(x): # define function
    for num in range(x): # for statement
        print('Hello') #log statement

print_hello_x_times(4) # call function

def print_hello_x_or_ten_times(x = 10):  # define function
    for num in range(x): # for statement
        print('Hello') #log statement

print_hello_x_or_ten_times() # call function
print_hello_x_or_ten_times(4) # call function


"""
Bonus section
"""

# print(num3) # log statement 
# num3 = 72 # variable declaration, number
# fruit[0] = 'cranberry' # change position 0 of fruit list to 'cranberry'
# print(person['favorite_team']) # log statement
# print(pizza_toppings[7]) # log statement
#   print(boolean) # log statement
# fruit.append('raspberry') # add 'raspberry' to fruit list
# fruit.pop(1) # remove position 1 from fruit list