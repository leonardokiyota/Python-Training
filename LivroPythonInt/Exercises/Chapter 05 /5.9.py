# -*- coding: utf-8 -*-
"""
    Imprima a divsão inteira do primeiro pelo segundo, assimcomo o resto da
    divisão. Utilize apenas os operadores de soma e subtração para calcular
    o resultado. O quociente da divisão de dois números é a qtd de vezes que
    podemos retirar o divisor do dividendo. Logo 20 / 4 = 5, uma vez que
    podemos subtrair 4 cinco vezes de 20.
"""

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

cont = 1
total = num1
div = 0
while cont < num2:
    total = total - num2
    cont += 1
    if total == 0:
        break

print("{} / {} é igual a {} ." .format(num1, num2, total))
