#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
    Cálculo de imposto.
'''

sal = float(input("Digite o salário para cálculo de imposto: "))
base =  sal
imposto = 0

if base > 3000:
    imposto = imposto + ((base - 3000) * 0.35)
    base = 3000

if base > 1000:
    imposto = imposto + ((base - 1000) * 0.20)

print("Salário: R$%6.2f - Imposto a pagar: R$%.2f."%(sal, imposto))
