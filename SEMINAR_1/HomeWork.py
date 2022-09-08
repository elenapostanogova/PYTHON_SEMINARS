# Task 1
#  Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

""" 
a = int(input('Введите номер дня недели: '))
if a == 6 or a == 7:
    print('да')
else:
    print('нет') 
"""

# Task 2
# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
""" 
for x in range(2):
    for y in range(2):
        for z in range(2):
            print(x, y, z, not (x or y or z) == (not x and not y and not z))
 """
# Task 3
# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

""" 
x = float(input('введите значение по оси x '))
y = float(input('введите значение по оси y '))
if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
elif x > 0 and y < 0:
    print(4) 
"""
 
# Task 4
#  Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
"""  
num = int(input('введите номер четверти '))
if num == 1:
    print('x > 0 and y > 0')
elif num == 2:
    print('x < 0 and y > 0')
elif num == 3:
    print('x < 0 and y < 0')
elif num == 4:
    print('x > 0 and y < 0') 
 """

# Task 5
# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

def inputCoordinates(x):
    xy = ["X", "Y"]
    a = []
    for i in range(x):
        number = float(input(f"Введите координату по {xy[i]}: "))
        a.append(number)
    return a

def calcLengthSegment(a, b):
    length = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** (0.5)
    return length

print("Введите координаты точки А")
pointA = inputCoordinates(2)
print("Введите координаты точки В")
pointB = inputCoordinates(2)

print(f"Длина отрезка: {format(calcLengthSegment(pointA, pointB), '.2f')}")
