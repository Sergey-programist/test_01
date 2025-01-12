from random import randint


numbers = []
length = int(input("Введите длинну случайного списка: "))
for i in range(length):
    numbers.append(randint(0, 10**10))

n = int(input("На сколько вы хотите частей разделить список?: "))
for i in range(0, length, length // n):
    start = i
    print(numbers[start:start + length // n]) 

