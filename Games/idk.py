

def greet():
    print(
        "Привет, вводи числа.А потом когда ты введёшь 0 ты узнаешь сумму всех чисел!\n"
    )


def input_game():
    sum_numbers = 0
    inp = None
    while inp != 0:
        inp = int(input())
        sum_numbers += inp
    print(f"Сумма введёных чисел = {sum_numbers}")

if __name__ == "__main__":
    greet()
    input_game()
