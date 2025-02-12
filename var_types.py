#string basics
basic = 'Hello, World!'
num_chars= len(basic) #counts the number of chars in the string

#string indexing
first_char = basic[0] #H brackets are used to index the string
last_char = basic[-1] #! negative numbers index from the end

#you cannot update a string, but you can reassign it
#basic[2] = 'z' will not work

#string concatenation
new_string = basic + ' I am here' #Hello, World! I am here

#string formatting 
number = 6
amount = 32.50
print(f'{number} burritos cost ${amount:.1f}')
print(f'{2**2=},{2**4=}') #2**2=4,2**4=16
print(f'{7600:,d}') #7,600 comma separator
print(f'{4:03d}') #004 leading zeros
print(f'{4:b}') #100 binary 
print(f'{31:x}') #1f hex 
print(f'{44:e}') #4.400000e+01 scientific notation


#list basics
fruits = ["apple", 20, "$20"] #lists can contain multiple data types
print(fruits[0]) #apple
fruits[1] = "banana" #lists are changeable
print(fruits) #['apple', 'banana', '$20']
fruits.append("orange") #add an item to the end of the list
print(fruits) #['apple', 'banana', '$20', 'orange']
fruits.remove("$20") #remove an item from the list, input is a value in the list
print(fruits) #['apple', 'banana', 'orange']
fruits.insert(2, "mango") #add an item at a specific index
print(fruits) #['apple', 'banana', 'mango', 'orange']
fruits.pop() #remove the last item from the list or a specific index
print(fruits) #['apple', 'banana', 'mango']
print(fruits.index("banana")) #1, returns the index of the first occurrence of the value

numbers = [1, 2, 3, 4, 5]
max_num = max(numbers) #5, use the max function to find the max value

#tuple basics, once created, you cannot change the elements in the list
fruits_tuple = ("apple", "banana", "mango")
#named tuple
from collections import namedtuple
Car = namedtuple("Car", ["make", "model", "year"])
car1 = Car("Toyota", "Camry", 2020)

#set basics, unordered collection of unique elements
nums = set([1, 2, 3, 4, 5, 5, 5]) #set([1, 2, 3, 4, 5]) , removes duplicates
nums1 = {6, 7, 7, 8, 9}
nums.add(10) #add an element to the set
nums.remove(5) #remove an element from the set
nums.pop() #remove an arbitrary element from the set
print(nums) #{1, 2, 3, 4, 10}

#dictionary basics
# dict = { key:value pairs }
person = {"name": "John", "age": 30, "city": "New York"}
print(person["name"]) #John
person['country'] = "USA" #add a new key value pair
person["name"] = "Jane" #update the value of a key
del person["city"] #remove a key value pair

#Type Conversions
num = 10 #int
num2 = 0.5 #float
num + num = 10 #int
num + num2 = 10.5 #float

num = str(num) #convert to string
num3 = int(num2) #convert to int
num4 = float(num3) #convert to float

