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
