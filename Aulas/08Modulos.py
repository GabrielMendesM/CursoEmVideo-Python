#from math import sqrt
import math
import random
from random import randint, randrange

'''
math.
    ceil = arredondar pra cima
    floor = arredondar pra baixo
    sqrt = raiz
'''
def MathF():
    num = int(input("Digite um número: "))
    raiz = math.sqrt(num)
    print(raiz)

def RandomF():
    print(random.random())
    print(random.random)

for x in range(10):
    RandomF()

catO = 20
catA = 10
hip = math.hypot(catO, catA)
print(f"HIPOTENUSA {hip}")
