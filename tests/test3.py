age = 12

def skoklet(a):
    if a < 13:
        return print('Ребёнок')
    if 12 < a < 18:
        return print('Подросток')
    if 17 < a < 50:
        return print('Взрослый')
    if a > 49:
        return print('Пожилой')

skoklet(age) 
