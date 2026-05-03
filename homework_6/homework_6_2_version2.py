# Конвертер із числа в дату

number = int(input('Enter a number: '))
endings = 'днів'

if 0 <= number <= 8640000:
    days, remaining = divmod(number, 86400)  # знаходимо дні і залишок
    hours, remaining = divmod(remaining, 3600)  # знаходимо години і залишок
    minutes, seconds = divmod(remaining, 60)  # знаходимо хвилини і секунди

if days % 10 == 1:
    endings = 'день'
elif 2 <= days % 10 <= 4:
    endings = 'дні'
print(f'{days} {endings}, {hours:02}:{minutes:02}:{seconds:02}')