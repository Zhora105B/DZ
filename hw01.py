__author__ = 'Dronov Egor Pavlovich'

# Задача-1: Ввести ваше имя и возраст в отдельные переменные,

# вычесть из возраста 18 и вывести на экран в следующем виде:
# "Василий на 2 года/лет больше 18"
# по желанию сделать адаптивный вывод, то есть "на 5 лет больше", "на 3 года меньше" и.т.д.

# TODO: код пишем тут...

name=input('ведите Ф.И.О')
vozrast=input('введите ваш возраст')
vozrast=int(vozrast)
c= vozrast-18
if c>0:
   print('{} на {} лет > 18'.format(name, c))
else:
   print('{} на {} лет < 18'.format(name, abs(c)))




# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Подсказка:
# * постарайтесь сделать решение через дополнительную переменную
#   или через арифметические действия
# Не нужно решать задачу так:
# print("a = ", b, "b = ", a) - это неправильное решение!

# TODO: код пишем тут...

a = int(input('Первое число'))
b = int(input('Второе число'))
а = а + в
b = a - b
a = a - b
print('Новое первое число', a)
print('Новое второе число', b)
    # Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...
import math

a=int(input('vvedite cjjficent a-'))
b=int(input('vvedite cjjficent b-'))
c=int(input('vvedite cjjficent c-'))

D=b**2-4*a*c

if D>0:
   x1=(-b+math.sqrt(D))/2*a
   x2=(-b-math.sqrt(D))/2*a
   print('x1=', x1)
   print('x2=',x2)
elif D==0:
    x=-b/2*a
    print()