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