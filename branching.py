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
