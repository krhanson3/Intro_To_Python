#if-else branches (general)
age = 20
if age >= 18:
    print('You are an adult')   # this line is executed
elif age < 18 and age > 12 : # elif is short for else if
    print('You are a minor')    # this line is not executed
else: 
    print('You are a child') # this line is not executed

x = 10
y = 20
if x!=y: # != means not equal to
    print('x is not equal to y')   # this line is executed
    print('this is extra') 
else:    
    print('x is equal to y')       # this line is not executed

 
#relational operators are used to compare values
# <, >, <=, >=, ==, !=  

#detecting ranges with branches 
num_outfits = int(input())

if num_outfits > 11:
    print('Must pack less')
elif 5 <= num_outfits <= 11:
    print('Larger suitcase')
elif 0 <= num_outfits <= 4:
    print('Medium suitcase')
elif num_outfits <= 0:
    print('Bad input')

#logical operators are used to combine conditions
# and, or, not
if num_outfits > 11:
    print('Must pack less')
elif (5 <= num_outfits) and (num_outfits <= 11):
    print('Larger suitcase')
elif (0 <= num_outfits) and (num_outfits <= 4):
    print('Medium suitcase')
elif (num_outfits < 0) or (num_outfits == 0):
    print('Bad input')

#membership operators
# in, not in
prices = [10, 20, 30, 40, 50]
if 20 in prices:
    print('20 is in prices')
if 100 not in prices:
    print('100 is not in prices')

#identity operators
# is, is not
x = 10
y = 10
if x is y:
    print('x and y are the same')
if x is not 20:
    print('x is not 20')    

animal = input()
adjective1 = input()

# Modify the following line
animals_string = ("Lane's favorite exhibit to look at when she goes to the zoo is "
                    "the {0} exhibit. She thinks the {0}s are {1} and cool.") #breaks the string up
# format() replaces the curly braces in a string with variables.
new_str = animals_string.format(animal, adjective1)
print(new_str)

#conditional expressions
# expr_when_true if condition else expr_when_false
# good practice is to restrict usage of conditional expressions to an assignment statement
if(y == 2):
    x = 10
else:
    x = 9*x
#can be written as
x = 10 if (y == 2) else 9*x
#only use when both branches update the same variable