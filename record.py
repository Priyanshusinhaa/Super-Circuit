from random import randint
from os import system
from time import sleep
from Circuit2.circuit2 import Circuit2


theta = [i for i in range(590)]
for i in range(90):
    a = randint(2,5)
    b = randint(2,6)
    circuit2 = Circuit2(b, a, theta)
    circuit2.draw()
    print() 

    print()
    print(f'Circuit2({b}, {a}, thetaList).draw()')
    sleep(3) 
    system('cls')
