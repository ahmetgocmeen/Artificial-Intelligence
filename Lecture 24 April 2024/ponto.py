import math
import random

def printListaPontos(lista):
    for p in lista:
        print(p, end=" ")
    print()

    
class Ponto:
    # x = 0
    # y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"Ponto({self.x},{self.y})"

    def posicao(self):
        return self.x, self.y   

    def dist(self, p):
        return math.sqrt((self.x - p.x)**2 + (self.y - p.y)**2)         



def calculaPerimetro(lista):
    total = 0
    for i in range(len(lista)-1):
        total = total + lista[i].dist(lista[i+1])
    total = total + lista[len(lista)-1].dist(lista[0])
    return total


p = Ponto(3,3)

print(p.x, '-', p.y)
print(p)
print(p.posicao())

p2 = Ponto(4,4)
print(p.dist(p2))

p.x = 1
p.y = 2
print(p.dist(p2))

lPontos = []
lPontos.append(Ponto(0,0))
lPontos.append(Ponto(0,4))
lPontos.append(Ponto(4,4))
lPontos.append(Ponto(4,0))
#lPontos.append(Ponto(random.randint(-10, 10), random.randint(-10, 10)))

printListaPontos(lPontos)

perimetro = calculaPerimetro(lPontos)
print('Perimetro:', perimetro)
