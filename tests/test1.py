import os


def greet():
    print("Добро пожалуйста в систему!\n")



def vhod():
    tries = 0
    password = "A15bsp50%/"
    enter = None
    while password != enter:
        enter = input("Пожалуйста введите пароль :")
        if password != enter:
            tries += 1
            print("Пароль неверный, попробуйте снова!")
        if tries == 5:
            print("Запускаю протокол выключения")
            os.system('shutdown /s /t 10')
    if password == enter:
        print("Вы успешно вошли в систему!")



if __name__ == '__main__':
    greet()
    vhod()
    