# -*- coding: utf-8 -*-
"""
    Acumuladores pág 91
"""

n = 1
soma = 0
while n <= 10:
    x = int(input("Digite o {} número: " .format(n)))
    soma = soma + x
    n = n + 1

print("Soma: {}". format(soma))