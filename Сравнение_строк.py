

stroka1 = input('Введите строку 1: ')
stroka2 = input('Введите строку 2: ')


def sravnenie_strok (str1, str2):
    if not ((isinstance(str1, str)) and (isinstance(str1, str))):
        return 0
    elif str1 == str2:
        return 1
    elif str1 != str2:
        if str2 == 'learn':
            return 3
        elif len(str1) > len(str2):
            return 2
        else:
            return None


otvet = sravnenie_strok(stroka1, stroka2)

print(otvet)

