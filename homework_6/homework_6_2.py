# Конвертер із числа в дату

from string import digits

num = input('Введіть число, яке > або = 0 і < 86640000: ')

# перевірка на число, в тому числі мінусове
flag_num = 0
for i in num[1:]:
    if num[0] == '-' or num[0] in digits:  # чи починається наша строка на - чи число
        if i not in digits:  # чи є всі інші елементи стоки числами
            flag_num += 1
            break
    else:
        flag_num += 1
        break

if flag_num == 0: # чи працюємо ми з числом
    if 0 <= int(num) < 86640000: # перевірка на відповідність діапазону
        num_day, remainder_num_day = divmod(int(num), (24 * 60 * 60)) # знаходимо дні і залишок
        num_hours, remainder_num_hours = divmod(int(remainder_num_day), (60 * 60)) # знаходимо години і залишок
        num_minutes, num_seconds = divmod(int(remainder_num_hours), 60) # знаходимо хвилини і секунди
        if 0 <= num_hours < 10: # формат 00:00:00 для годин
            num_hours = str(num_hours).zfill(2)
        if 0 <= num_minutes < 10: # формат 00:00:00 для хвилин
            num_minutes = str(num_minutes).zfill(2)
        if 0 <= num_seconds < 10: # формат 00:00:00 для секунд
            num_seconds = str(num_seconds).zfill(2)
        print(f'{num_day} днів, {num_hours}:{num_minutes}:{num_seconds}')
    else:
        print('Не вірно введено число - поза діапазоном')
else:
    print('Ви ввели не число')


