#reverse binary 
x = int(input())
while x > 0:
    print(x%2, end='')
    x = x//2
print()

#printing a triangle
triangle_char = input("Enter a character:\n") 
triangle_height = int(input("Enter triangle height:\n"))
print("")

#added space after triangle_char to make the triangle look better
triangle_string = triangle_char + ' '
while triangle_height > 0:
    print(triangle_string)
    #increasing the number of triangle_char by 1
    triangle_string = triangle_string + triangle_char + ' '
    #decreasing the count of triangle_height by 1
    triangle_height -= 1