#user-defined functions
def minutes_as_hours(minutes):
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours}h {remaining_minutes}m"

minutes = int(input("Enter minutes: "))
print(minutes_as_hours(minutes))

#print functions
def print_greeting(name):
    print(f"Hello, {name}!")

name = input("Enter your name: ")
print_greeting(name)
#helpful to avoid code duplication

#multiple values in a function
def print_college_location(city, college):
    print(f'{city} is the location of {college} College.')

city1 = input()
city2 = input()
college1 = input()
college2 = input()

print_college_location(city1, college1)
print_college_location(city2, college2)

#polymorphic functions
def add(a, b):
    return a + b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", add(a, b)) #prints the sum of two numbers

stringa = input("Enter first string: ")
stringb = input("Enter second string: ")
print("Concatenated string:", add(stringa, stringb)) #prints the concatenated string

def multiples(n, m):
    return n * m

n = int(input("Enter multiplier: "))
m = input("Enter string: ")
print("Repeated string:", multiples(m, n)) #prints the repeated string

#arbitrary arguments
def print_stats(name, **stats):
    print(f"Name: {name}")
    for key, stat in stats.items():
        print(f'{key}: {stat}')

print_stats("Alice", age=25, height=5.5, weight=130)
#output will be:
#Name: Alice age: 25 height: 5.5 weight: 130

#returning multiple values
student_grades = [75, 84, 92, 88, 76]
def grade_stats(grades):
    avg = sum(student_grades) / len(grades)
    tmp = 0
    for grade in grades:
        tmp += (grade - avg) ** 2
    std_dev = (tmp / len(grades)) ** 0.5
    return avg, std_dev

average, standard_deviation = grade_stats(student_grades)
print(f"Average: {average:.2f}", end=' ')
print(f"Standard Deviation: {standard_deviation:.2f}")
#output will be: 
#Average: 83.00 Standard Deviation: 6.92
