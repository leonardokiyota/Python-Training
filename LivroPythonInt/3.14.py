#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
   Escreva um programa que pergunte a qtd de Km percorridos. qtd de dias. calcular
   preco a pagar, sabendo que o carro custa R$60,00 por dia e R$0.15 por KM rodado.
'''

dias = int(input("Digite a quantidade de dias: "))
km = float(input("Digite o KM rodado: "))

print("A quantidade de dia(s) foi de %d e a KM rodado foi de %.2f e o valor total a pagar é de R$%.2f."%(dias, km, (dias * 60) + (km * 0.15)))

   
