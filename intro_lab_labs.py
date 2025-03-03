#basic input output 
x = int(input('Enter x: '))
print('x doubled is:', (2 * x))

#practicing formatting output
print("NO PARKING")
print("2:00 - 6:00 a.m.")

#math with float formatting
mileage = float(input())
cost_of_gas = float(input())
cost_for_20_gal = (20 / mileage) * cost_of_gas
print(f'{cost_for_20_gal:.2f}')

#floor division with integers 
user_num = int(input())
div_num = int(input())
div1 = user_num//div_num
div2 = div1//div_num
div3 = div2//div_num
print(div1, div2, div3)

#writing expressions + formatting for PEMDAS
age = float(input())
weight = float(input())
heart_rate = float(input())
minutes = float(input())
calories = (((age*0.2757)+(weight*0.03295)+(heart_rate*1.0781)-75.4991)*minutes)/8.368
print(f"Calories: {calories:.2f} calories")

#math functions
import math
x = float(input())
y = float(input())
z = float(input())
val1 = math.pow(x,z)
val2 = math.pow(x,math.pow(y,z))
val3 = abs(x-y)
val4 = math.sqrt(val1)
print(f'{val1:.2f} {val2:.2f} {val3:.2f} {val4:.2f}')