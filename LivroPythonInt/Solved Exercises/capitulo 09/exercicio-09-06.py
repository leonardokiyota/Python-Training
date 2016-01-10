##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: exercicios_resolvidos\capitulo 09\exercicio-09-06.py
##############################################################################
LARGURA=79
entrada=open("entrada.txt")
for linha in entrada.readlines():
    if linha[0]==";":
        continue
    elif linha[0]==">":
        print(linha[1:].rjust(LARGURA))
    elif linha[0]=="*":
        print(linha[1:].center(LARGURA))
    elif linha[0]=="=":
        print("=" * 40)
    elif linha[0]==".":
        input("Digite algo para continuar")
        print()
    else:
        print(linha)
entrada.close()
