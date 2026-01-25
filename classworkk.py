'''
print('Привіт, Ігор!')
print(10)

print(10 + 7)

if 10 > 5: print('10 > 5')

a = 10
b = 15
print('b') if b > a else print('a')

day = 5
match day:
    case 1: print('ПН')
    case 2: print('вт')
    case 3: print('ср')
    case 4: print('чт')
    case 5: print('пт')
    case 6: print('сб')
    case 7: print('нд')
'''

needed_potatoes = int(input('Скільки картоплі чистити? '))
pealed_potatoes = 0

while pealed_potatoes < needed_potatoes:
    print('Беремо картоплю...')
    is_rotten = input('Картопля гнила? ')
    if is_rotten == 'так':
        print('Викидаємо!')
        continue
    print('Чистимо картоплю...')
    pealed_potatoes += 1
    print(f'Готово! Почищено: {pealed_potatoes}')
    is_tired = input('Ви втомились? ')
    if is_tired == 'так':
        break
else:
    print('Почистили ВСЮ картоплю!')

print(f'Почистили {pealed_potatoes} картоплі!')


'''
while True:
    num1 = float(input('Введіть перше число: '))
    num2 = float(input('Введіть друге число: '))
    action = input('Введіть операцію (+, -, *, /): ')

    match action:
        case '+': print(f'{num1} + {num2} = {num1 + num2}')
        case '-': print(f'{num1} - {num2} = {num1 - num2}')
        case '*': print(f'{num1} * {num2} = {num1 * num2}')
        case '/': 
            if num2 == 0: print('Неможна ділити на нуль!')
            else: print(f'{num1} / {num2} = {num1 / num2}')
        case _: print('Некоректна операція')

    q = input('Input \'q\' to quit or press Enter to continue: ')
    if q == 'q':
        break
'''