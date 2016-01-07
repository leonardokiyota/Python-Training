#!/usr/bib/env python3
# -*- encoding: utf-8 -*-
'''
   Escreva um programa que calcule o tempo de vida de um fumante. Pergunte a qtd
   de cigarro por dia e quantos anos já fumou. Considere perder 10 min de vida
   a cada cigarro. Calcule quantos dias de vida perderá. Exiba total de dias.
'''

qtddia = int(input("Digite quantos cigarros você fuma por dia: "))
anos = int(input("Quantos anos que você fuma: "))
print("Você fumou %d em %d anos e você perdeu %d dias de vida."%((qtddia * anos * 365), anos, (qtddia * anos * 365) * 10 - (365 * anos)))
