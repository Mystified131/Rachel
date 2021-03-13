import random
from RandFunct import random_number
from RandFunct2 import random_number2

hopl = [(0, -2), (0, -1), (0, 0), (0 , 1,), (0, 2), (1, -2), (1, -1), (1, 0), (1, 1), (1, 2), (2, -2), (2, -1), (2, 0), (2, 1), (2, 2), (-2, -2), (-2, -1), (-2, 0), (-2, 1), (-2, 2), (-1, -2), (-1, -1), (-1, 0), (-1, 1), (-1, 2)]

#mapl can be any list

mapl = []

for x in range(100):
    mapl.append(x)

moves = 50

fst = random_number(len(mapl))

fval = mapl[fst]

for ctr in range(moves):
    hopran = random_number(len(hopl))
    aval = sum(int(i) for i in hopl[hopran])
    fval += aval
    print(fval)

print(fval)


