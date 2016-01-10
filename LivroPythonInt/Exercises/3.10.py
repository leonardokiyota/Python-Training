#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

'''
   Escreva um programa que calcule o aumento de um salário. Deve perguntar
   o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do
   novo salário.
'''

sal = float(input("Digite o valor do salário: "))
porce = int(input("Digite o valor da porcentagem: "))
aumento = porce * sal / 100
print("O salário R$%.2f teve aumento de R$%.2f e o novo valor é R$%.2f . "%(sal, aumento, sal + aumento))
