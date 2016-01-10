##!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
    Faça um programa que leia dois números. Imprima o resultado da multiplicação.
    Utilize os operadores de soma e subtração para calcular o reultado.
    Ex: 4 x 5 = 4 + 4 + 4 + 4 + 4 = 5 + 5 + 5 + 5.
'''

num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))

cont = 0
total = 0
while cont < num1:
    total = num2 + total
    cont += 1

print("{} x {} é igual a {} ." .format(num1, num2, total))
