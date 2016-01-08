# -*- coding: utf-8 -*-

"""
     Faça um Programa que peça 2 números inteiros e um número real. 
     Calcule e mostre:

     - O produto do dobro do primeiro com metade do segundo .
     - A soma do triplo do primeiro com o terceiro.
     - O terceiro elevado ao cubo.
"""

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))
num3 = float(input("Digite um número real: "))

print("O produto do dobro do primeiro com metade do segundo é: {}". format((num1 * 2) / (num2 / 2)))
print("A soma do triplo do primeiro com o terceiro é: {}" .format((num1 * 3) + num3))
print("O terceiro elevado ao cubo é: {}".format(num3 ** 3))