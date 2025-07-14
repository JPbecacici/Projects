# Python Temperature Converter

unit = input('Is this temperature Celsius or Fahrenheit (C/F): ').upper()
temp = float(input('Enter the temperature: '))

if unit == 'C':
    temp = round((temp * 9/5) + 32, 1)
    print(f'The temperature in Fahrenheit is: {temp}Fº')

elif unit == 'F':
    temp = round((temp - 32) * 5/9, 1)
    print(f'The temperature in Celsius is: {temp}Cº')

else:
    print(f'{unit} is an invalid unit of messurement!')