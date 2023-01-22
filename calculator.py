x = float(input('Первое число: '))
y = float(input('Второе число: '))
operation = input('Операция: ')

result = None

if operation == '+':
    result = x + y
elif operation == '-':
    result = x - y
elif operation == '*':
    result = x * y
elif operation == '/':
    result = x / y
else:
    print('Unsupported operation')

if result is not None:
    print('Результат', result)
