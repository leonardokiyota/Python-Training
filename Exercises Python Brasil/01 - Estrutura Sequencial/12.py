# -*- coding: utf-8 -*-
"""
    Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso 
    ideal, usando a seguinte fórmula: (72.7*altura) - 58 Tendo como dados de entrada a altura 
    e o sexo de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as 
    seguintes fórmulas:

            Para homens: (72.7*h) - 58
            Para mulheres: (62.1*h) - 44.7 (h = altura)
            Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do peso.
"""

altura = float(input("Digite a sua altura: "))
peso = float(input("Digite o seu peso: "))
sexo = input("Digite F para Feminino ou M para masculino: ")


def calculapeso(altura, sexo):
    p_ideal = 0
    if sexo == 'F':
        p_ideal = 62.1 * altura - 44.7
                
    elif sexo == 'M':
        p_ideal = 72.7 * altura - 58
        
    return (p_ideal)
       
 
def verifica():
    pesoi = calculapeso(altura, sexo)
    if peso >= pesoi:
        print("Você está acima do peso!")
        print("O seu peso ideal é {:.3f} e você está pesando {:.3f}.".format(pesoi, peso))
    else:
        print("Você está abaixo do peso!")
        print("O seu peso ideal é {:.3f} e você está pesando {:.3f}." .format(pesoi, peso))

def main():
    verifica()

if __name__ == '__main__':
    main()

        
        