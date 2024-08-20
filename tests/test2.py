print("Напиши сколько тебе лет и я скажу кто ты...")

age = int(input("Сколько тебе лет?    "))

def skoklet(a):
    if a < 13:
        return print('Ты ребёнок')
    if 12 < a < 18:
        return print('Ты подросток')
    if 17 < a < 50:
        return print('Ты взрослый')
    if a > 49:
        return print('Ты дед')

skoklet(age) 
