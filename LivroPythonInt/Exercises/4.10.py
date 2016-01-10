#!/usr/binenv python3
# -*- encoding: utf-8 -*-

'''
    Escreva um programa que calcule o preço a pagar pelo fornecimento de energia.
    Pergunte o KWh consumida e o tipo de instalação. R para residências,
    I para Industria e C para comércio. Calcule o preço a pagar com a tabela
    a seguir.

    TIPO          Faixa(KWh)      Preço
    Residencia     até 500          R0.40
    Residencia     acima 500        R0.65
    Comercio       até 1000         R0.55
    Comércio       acima de 1000    R0.60
    Industria      até 5000         R0.55
    Industria      acima de 5000    R0.60

'''

print("Digite R para Residência.")
print("Digite I para Industria.")
print("Digite C para Comércio")
consumo = int(input("Digite o consumo: "))
tipo = input("Digite o tipo: ")

if tipo == "R":
    if consumo > 0 and consumo <= 500:
        print("É uma residência e o seu consumo foi de %d e o total a pagar é R$%.2f."%(consumo, consumo * 0.40))
    else:
        print("É uma residência e o seu consumo foi de %d e o total a pagar é R$%.2f."%(consumo, consumo * 0.65))
        
elif tipo == "C":

    if consumo > 0 and consumo <= 1000:
        print("É uma Comércio e o seu consumo foi de %d e o total a pagar é R$%.2f."%(consumo, consumo * 0.55))
    else:
        print("É uma Comércio e o seu consumo foi de %d e o total a pagar é R$%.2f."%(consumo, consumo * 0.60))

elif tipo == "I":

    if consumo > 0 and consumo <= 5000:
        print("É uma Indústria e o seu consumo foi de %d e o total a pagar é R$%.2f."%(consumo, consumo * 0.55))
    else:
        print("É uma Indústria e o seu consumo foi de %d e o total a pagar é R$%.2f."%(consumo, consumo * 0.60))
    
else:
    print("Opção Inválida!")


