
vopros_otvet = {"Как дела?": "Хорошо!", "Что делаешь?": "Программирую", "Что на завтра": "Не решил ещё"}


def ask_user():
    otvet = ' '
    while otvet != "Хорошо":
        otvet = input("Пользователь: ")
        for key in vopros_otvet.keys():
            if otvet == key:
                print("Программа: ", vopros_otvet[key])




ask_user()