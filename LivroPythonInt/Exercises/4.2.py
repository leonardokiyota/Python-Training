#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
    Escreva um programa que pergunte a velocidade do carro. Caso ultrapasse
    80 Km/h, exiba uma mensagem dizendo que o condutor foi multado.
    Nesse caso, exiba p valor da multa, cobrando R$5,00 por km excedido.
'''
vel = float(input("Digite a velocidade: "))

if vel <= 80:
    print("Parabéns! Você não está excedendo a velocidade permitida!")
if vel > 80:
    print("Voce excedeu a velocidade máxima permitida e a sua multa a pagar é de R$%.2f ."%((vel - 80)*5))
