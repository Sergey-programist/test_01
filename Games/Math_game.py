from random import randint


def greet() -> None:
    print("Привет, давай ты будешь моим калькулятором? (это игра)\n")


def play(score: int) -> int:
    a = randint(2, 20)
    b = randint(2, 10)
    operations = ("+", "-", "*", "/")

    selected_operation = randint(0, 3)
    question = (f"{a} {operations[selected_operation]} {b}")

    print(question)

    if operations[selected_operation] == "+":
        correct_ans = a + b 
        
    elif operations[selected_operation] == "-":
        correct_ans = a - b 
        
    elif operations[selected_operation] == "*":
        correct_ans = a * b 
        
    elif operations[selected_operation] == "/":
        correct_ans = a / b 
        
    user_ans = float(input())

    if user_ans == correct_ans:
        score += 1
        print("Правильно!")
    else:
        print("Неправильно!")

    return score


def print_current_score(score: int) -> None:
    print(f"Твой счёт: {score}\n")


if __name__ == '__main__':
    score = 0
    greet()
    while True:
        score = play(score) 
        print_current_score(score)
        