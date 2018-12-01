

age = int(input('Введите ваш возраст: '))

def status(vozrast):
    if 0 < vozrast < 6:
        return 'Детский сад'
    elif 6 <= vozrast <= 18:
        return 'Школа'
    elif 19 <= vozrast <= 25:
        return 'ВУЗ'
    elif vozrast > 25:
        return 'Работа'

vivod = status(age)

print(vivod)
