#data types
name = "kat" #string
age = 22 #int
wage = 2.35 #float
z = 35e3
fruits = ["apple", "banana", "cherry"] #list
veggies = ("squash", "tomato", "cucumber") #tuples
w = {"name" : "John", "age" : 36} #dict
x = range(6) #range
y = False #bool

#basic input output
name = input('enter your name\n')
print('your name is', name)

#changes string input into integer & variable assignment 
num1 = int(input('enter a number\n')) 
num2 = int(input('enter another number'))
#math
print("the numbers", num1, "and", num2,"added is", num2+num1)

#syntax 
print('this is how to', end=' ')
print('write on one line w/ multiple lines of code')
#you can also include syntax adjusters like \t for tab or \n for new line

#digits after float
gas_pressure = 9.61351354
print('Gas pressure is', f'{gas_pressure:.3f}')
#sets output to only include three digits after decimal

## more math 
a = 20/10 = 2.0 #simple divison results in a float
b = 22//10 = 2  #rounds down to the neareste whole number
c = 23 % 10 = 3 #outputs the leftover amount 

## digits
