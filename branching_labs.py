#removing grey from color code and displaying the remaining colors
red = int(input())
green = int(input())
blue = int(input())

if(red<green) and (red<blue):
    green = green - red
    blue = blue - red
    red = red-red
elif(green<red) and (green<blue):
    blue = blue - green
    red = red-green
    green = green-green
elif(blue<red) and (blue<green):
    red = red - blue
    green = green - blue 
    blue = blue - blue 
elif(red==blue) and (red==green):
    red = 0
    green = 0 
    blue = 0

print(f'{red} {green} {blue}')

#giving the correct change in coins for a given amount
amount = int(input())
if(amount == 0):
    print('No change')
dollars = amount//100 
if(dollars>1):
    print(f'{dollars} Dollars')
elif(dollars==1):
    print(f'{dollars} Dollar')
amount = amount % 100
quarters = amount//25 
if(quarters>1):
    print(f'{quarters} Quarters')
elif(quarters==1):
    print(f'{quarters} Quarter')
amount = amount%25 
dimes = amount//10 
if(dimes>1):
    print(f'{dimes} Dimes')
elif(dimes==1):
    print(f'{dimes} Dime')
amount = amount%10 
nickels = amount//5 
if(nickels>1):
    print(f'{nickels} Nickels')
elif(nickels==1):
    print(f'{nickels} Nickel')  
amount = amount%5 
pennies = amount//1 
if(pennies>1):
    print(f'{pennies} Pennies')
elif(pennies==1):
    print(f'{pennies} Penny')


#auto services invoice 
print('Davy\'s auto shop services')
print('Oil change -- $35')
print('Tire rotation -- $19')
print('Car wash -- $7')
print('Car wax -- $12')

service1 = input('Select first service:\n')
service2 = input('Select second service:\n')
total = 0

print('\nDavy\'s auto shop invoice\n')
if service1 == 'Oil change':
    print('Service 1: Oil change, $35')
    total += 35
elif service1 == 'Tire rotation':
    print('Service 1: Tire rotation, $19')
    total += 19
elif service1 == 'Car wash':
    print('Service 1: Car wash, $7')
    total += 7
elif service1 == 'Car wax':
    print('Service 1: Car wax, $12')
    total += 12
elif service1 == '-':
    print('Service 1: No service')

if service2 == 'Oil change':
    print('Service 2: Oil change, $35')
    total += 35
elif service2 == 'Tire rotation':
    print('Service 2: Tire rotation, $19')
    total += 19
elif service2 == 'Car wash':
    print('Service 2: Car wash, $7')
    total += 7  
elif service2 == 'Car wax':
    print('Service 2: Car wax, $12')
    total += 12
elif service2 == '-':
    print('Service 2: No service')

print(f'\nTotal: ${total}')


#seasons based on month and day 
input_month = input()
input_day = int(input())

months_31 = ['January', 'March', 'May', 'July', 'August', 'October', 'December']
months_30 = ['April', 'June', 'September', 'November']
months_28 = ['February']
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

if (input_month not in months) or (input_day < 1 or input_day > 31):
    print('Invalid')
    exit()
elif (input_month in months_31) and (1 < input_day > 31):
    print('Invalid')
    exit()
elif (input_month in months_30) and (1 < input_day > 30):
    print('Invalid')
    exit()
elif (input_month in months_28) and (1 < input_day > 28):
    print('Invalid')
    exit()

if (input_month == 'March ' and input_day >= 20) or (input_month == 'April') or (input_month == 'May') or (input_month == 'June' and input_day < 21):
    print('Spring')
elif (input_month == 'June' and input_day >= 21) or (input_month == 'July') or (input_month == 'August') or (input_month == 'September' and input_day < 22):
    print('Summer')
elif (input_month == 'September' and input_day >= 22) or (input_month == 'October') or (input_month == 'November') or (input_month == 'December' and input_day < 21):
    print('Autumn')
elif (input_month == 'December' and input_day >= 21) or (input_month == 'January') or (input_month == 'February') or (input_month == 'March' and input_day < 20):
    print('Winter')