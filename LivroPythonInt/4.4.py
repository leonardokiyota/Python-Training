#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
    Escreva um programa que pergunte o salário do funcionário e calcule o valor
    do aumento. Para salários superiores a R$1.250,00 calcule um aumento de
    10%. Para os inferiores ou iguais aumento de 15%.
'''

sal = float(input("Digite o seu salário: "))

if sal <= 1250:
    aumento = sal * 15 / 100
    print("O salário terá 15%% de aumento que é de R$%.2f o novo salário é de R$%.2f ."%(aumento, sal + aumento))

if sal > 1250:
    aumento = sal * 10 / 100
    print("O salário terá 10%% de aumento que é de R$%.2f o novo salário é de R$%.2f ."%(aumento, sal + aumento))
