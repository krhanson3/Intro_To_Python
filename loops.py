x = int(input())  # Input statement
while x != 0:  # Loop expression
    # Loop body: Sub-statements to execute
    # if the loop expression evaluates to True
    print(x)
# Statements to execute after the expression evaluates to False

x = 3
while x >= 1:
    x = x - 1
    #loop will execute 3 times

#sentinel value = a value that signals the end of the loop
user_input = input("Enter a character ('q' for quit): ")
while user_input != 'q':
    print(user_input)
    user_input = input("Enter a character ('q' for quit): ")
    #loop will execute until user enters 'q'


target = int(input())
n = int(input())
step = 3
while n > target:
    print(n * 2)
    n -= step
#loop will execute until n is less than or equal to target

#for loops 
for name in ['Alice', 'Bob', 'Charlie']:
    print(name)
#loop will execute 3 times, once for each name in the list

#looping through a dictionary
cities = {
    'Chicago': 438,
    'Paris': 5259,
    'Austin': 958,
}

best = ''
distance = 0
for city in cities:
    if cities[city] > distance:
        best = city
        distance = cities[city]
print(best, distance)


#nested loops
stop = int(input())

for a in range(4): #outer loop - range = 0, 1, 2, 3
    result = 0
    for b in range(3):  #inner loop - range = 0, 1, 2
        result += b    #
    result += a
    print(result)
    if result > stop: #breaks the outer loop
        break


threshold = int(input())

for a in range(0, 4):
    print(a + 1, end=': ')
    for b in range(0, 2):
        if a > threshold:
            print('_,', end='')
            continue
        print(b, end=',')

    print() 


#else block in loops
result = 0
n = 1
while n > -7:
    print(n, end=' ')
    result -= 4
    if result < -9:
        print('$')
        break
    n -= 1
else: #executes if the loop completes without breaking
    print(f'/ {result}')
print('done')

#index and value in loops
input_count = int(input())

list_visitors = []
for i in range(input_count):
    list_visitors.append(input())

for (idx, name) in enumerate(list_visitors): #enumerate returns index and value
    if idx % 2 != 0:
        print(f'{name} is scheduled for Morning')
    else:
        print(f'{name} is scheduled for Afternoon')