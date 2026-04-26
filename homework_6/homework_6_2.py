# Конвертер із числа в дату

from string import digits
num = input('Введіть число, яке > або = 0 і < 86640000: ')
flag = 0
for i in num[1:]:
    if num[0] == '-' or num[0] in digits:  # перевірка на число, в тому числі мінусове
        if i not in digits:
            flag += 1
            break
    else:
        flag += 1
        break

if flag == 0:
    if 0 <= int(num) < 86640000: # перевірка на відповідність діапазону
        num_day, remainder_num_day = divmod(int(num), (24 * 60 * 60))
        num_hours, remainder_num_hours = divmod(int(remainder_num_day), (60 * 60))
        num_minutes, num_seconds = divmod(int(remainder_num_hours), 60)
        if 0 <= num_hours < 10:
            num_hours = str(num_hours).zfill(2)
        if 0 <= num_minutes < 10:
            num_minutes = str(num_minutes).zfill(2)
        if 0 <= num_seconds < 10:
            num_seconds = str(num_seconds).zfill(2)
        print(f'{num_day} днів, {num_hours}:{num_minutes}:{num_seconds}')
    else:
        print('Не вірно введено число - поза діапазоном')
else:
    print('Ви ввели не число')


