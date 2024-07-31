x = 2 # для прямоугольных
y = 3
z = 2

r = 10 # для круго-подобных

def per_k(A):
    return print("Площадь квадртата =",A*2)

def per_p(A, B):
    return print("Площадь прямоугольника =",A*B)

def per_pt(A, B):
    return print("Площадь прямоугольного треугольника =",(A*B)/2)

def per_kr(A):
    return print("Площадь круга ≈",3.1415926535 * (A*A))

per_k(x)
per_p(x, y)
per_pt(x, y)
per_kr(r)

