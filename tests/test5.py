from time import sleep

def greet():
    print("Добро пожаловать в THE обратный отсчёт")

def proggram():
    time = int(input("Обратный отсчёт с : "))
    if time < 0:
        print("Ошибка: отрицательное время")
    elif time == 0:
        print("Ошибка: время равно нулю")
    elif time > 0:
        while not(time < 1):
            print(time)
            time -= 1
            sleep(1)
        print("Время вышло!")

if __name__ == '__main__':
    greet()
    proggram()