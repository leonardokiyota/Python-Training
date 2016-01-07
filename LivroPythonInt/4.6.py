#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
    Escreva um programa que pergunte a distância que se deseja em KM. Calcule
    o preço da passagem, cobrando R$0.50 por km até 200KM, e R0.45 para viagens
    mais longa.
'''

km = int(input("Digite a distância da viagem: "))

if km <= 200:
    print("O valor da viagem é de R$%.2f ."%(km * 0.50))
else:
    print("O valor da viagem é de R$%.2f ."%(km * 0.45))
