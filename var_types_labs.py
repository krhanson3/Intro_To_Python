#Input and Formatted output: Right-Facing Arror
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