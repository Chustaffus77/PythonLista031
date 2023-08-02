#9) Fazer um algoritmo que pergunte 1 número e apresente:
#a) O próprio número
#b) O quadrado deste número
#c) A raiz quadrada deste número


import math
num = float(input("Insira um número, por favor:"))

p = math.pow(num,2)

r = math.sqrt(num)

print(num)
print(p)
print(r)

print("Esses são,respectivamente, o número em si, o quadrado desse número e por fim a raíz quadrada dele.")

