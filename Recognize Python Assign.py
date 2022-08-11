num1 = 42 # variable declaration, number initialized
num2 = 2.3 # variable declaration, decimal initialized
boolean = True # variable declaration, boolean initialized
string = 'Hello World' # variable delcaration, string initialized

# variable delcaration, list initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
# variable declaration, dictionary initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
# variable delcaration, tuple initialized
fruit = ('blueberry', 'strawberry', 'banana')
print(type(fruit)) # print to console, type check
print(pizza_toppings[1]) # print to console, access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # print to console, dictionary access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary change value
print(fruit[2]) # print to console, tuple access value

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
# conditional if, evaluation, print to console, conditional else, print to console

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
# conditional if, evaluation, print to console, conditional elif, print to console, conditional else, print to console

for x in range(5): # for loop starts at 0 and goes to 5
    print(x)
for x in range(2,5): # for loop starts at 2 and goes to 5
    print(x)
for x in range(2,10,3): # for loop starts at 2 and goes to 10, increments by 3
    print(x)
# variable declaration
x = 0
while(x < 5): # while loop 
    print(x) # prints to console
    x += 1 # increments x by 1


pizza_toppings.pop() # list delete value
pizza_toppings.pop(1) # list deletes value at index

print(person) # print to console at dictionary
person.pop('eye_color') # dictionary delete value
print(person) # print to console of dictionary

for topping in pizza_toppings: # for loop through list
    if topping == 'Pepperoni': # conditional if
        continue # continues
    print('After 1st if statement') # print to console
    if topping == 'Olives': # conditional if
        break # stops loops

def print_hello_ten_times():#declaration of function
    for num in range(10): # for loop starts at 0 going up to 10
        print('Hello') # print to console 

print_hello_ten_times() # function call

def print_hello_x_times(x): # function declaration
    for num in range(x): # for loop until the number in (x)
        print('Hello') # print to console

print_hello_x_times(4) # function call of 4

def print_hello_x_or_ten_times(x = 10): # function declaration with default parameter
    for num in range(x): # for loop until (x)
        print('Hello') # print to console

print_hello_x_or_ten_times() # function call goes to 10
print_hello_x_or_ten_times(4) # function call goes to 4


"""
Bonus section
"""

# print(num3) # print num3 to console
# num3 = 72 # function declaration, number initialized
# fruit[0] = 'cranberry' # dictionary change value
# print(person['favorite_team']) # print to console, dictionary access value
# print(pizza_toppings[7]) # print to console, tuple access value
#   print(boolean) # print to console
# fruit.append('raspberry') # list add value
# fruit.pop(1)0 # list delete value at index