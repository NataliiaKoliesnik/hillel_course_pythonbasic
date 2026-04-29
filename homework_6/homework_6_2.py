# Конвертер із числа в дату

from string import digits

num = input('Введіть число, яке > або = 0 і < 86640000: ')
str_day = str()
# перевірка на число, в тому числі мінусове
if 0 <= int(num) < 86640000: # перевірка на відповідність діапазону
    num_day, remainder_num_day = divmod(int(num), (24 * 60 * 60)) # знаходимо дні і залишок
    num_hours, remainder_num_hours = divmod(int(remainder_num_day), (60 * 60)) # знаходимо години і залишок
    num_minutes, num_seconds = divmod(int(remainder_num_hours), 60) # знаходимо хвилини і секунди
    if 11 <= num_day <= 14:
        str_day = 'днів'
    elif num_day % 10 == 1:
        str_day = 'день'
    elif 2 <= num_day % 10 <= 4:
        str_day = 'дні'
    else:
        str_day = 'днів'
    if 0 <= num_hours < 10: # формат 00:00:00 для годин
        num_hours = str(num_hours).zfill(2)
    if 0 <= num_minutes < 10: # формат 00:00:00 для хвилин
        num_minutes = str(num_minutes).zfill(2)
    if 0 <= num_seconds < 10: # формат 00:00:00 для секунд
        num_seconds = str(num_seconds).zfill(2)
    print(f'{num_day} {str_day}, {num_hours}:{num_minutes}:{num_seconds}')
else:
    print('Не вірно введено число - поза діапазоном')



