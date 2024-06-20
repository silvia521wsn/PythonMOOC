tem_fa = int(input('Please type in a temperature (F): '))
tem_ce = (tem_fa - 32)*5/9
print(f'{tem_fa} degrees Fahrenheit equals {tem_ce} degrees Celsius')
if tem_ce < 0:
    print('Brr! It\'s cold in here!')