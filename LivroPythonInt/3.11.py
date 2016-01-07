#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
   Faça um programa que solicite o preço de uma mercadoria e o percentual
   de desconto. Exiba o valor do desconto e o preço a pagar.
'''

preco = float(input("Digite o valor da mercadoria: "))
porc = int(input("Digite o valor do desconto: "))
desc = preco * porc / 100

print("A mercadoria custa R$%.2f e teve desconto de R$%.2f e o valor à pagar com o desconto é de R$%.2f."%(preco, desc, preco - desc))
   
