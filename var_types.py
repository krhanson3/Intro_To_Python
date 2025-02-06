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