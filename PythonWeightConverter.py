#Python Weight Converter

weight = float(input('Enter your weight: '))
unit = input('Kilogram or Pounds? (K or L): ').upper()

if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f'Your weight is {round(weight, 2)} {unit}')
elif unit == 'L':
    weight == weight / 2.205
    unit = 'Kgs.'
    print(f'Your weight is {round(weight, 2)} {unit}')
else:
    print(f'{unit} is invalid!')