#Input and Formatted output: Right-Facing Arrow
base_char = input()
head_char = input()

row1 = '      ' + head_char
row2 = base_char+base_char+base_char+base_char+base_char+base_char+head_char+head_char
row3 = base_char+base_char+base_char+base_char+base_char+base_char+head_char+head_char+head_char

print(row1)
print(row2)
print(row3)
print(row2)
print(row1)

#Phone Number Formatting
phone_number = int(input())
last_four = phone_number%10000
newnum = phone_number//10000
mid3 = newnum%1000
areacode = newnum//1000
ac = str(areacode)
mid = str(mid3)
lf = str(last_four)
print('(' + ac + ')', mid + '-' + lf)

#Input and Formatted Output: Caffeine Level
caffeine_mg = float(input())
print(f'After 6 hours: {caffeine_mg/2:.2f} mg') #output = 50.00
print(f'After 12 hours: {caffeine_mg/4:.2f} mg') #output = 25.00
print(f'After 24 hours: {caffeine_mg/16:.2f} mg') #output = 6.25

#Input and Formatted Output: Real Estate Summary
current_price = int(input())
last_months_price = int(input())
change = current_price-last_months_price
print(f'This house is ${current_price}. The change is ${change} since last month.')
monthly = (current_price * 0.051) /12
print(f'The estimated monthly mortgage is ${monthly:.2f}.')

#simple statistics 
num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())
product = num1 * num2 * num3 * num4
average = (num1 + num2 + num3 + num4)/4
print(f'{round(product):.0f} {round(average):.0f}') #output ex. = 24 6
print(f'{product:.3f} {average:.3f}') #output ex. = 24.000 6.000