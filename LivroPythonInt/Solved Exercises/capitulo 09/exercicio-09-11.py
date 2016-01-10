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
# Arquivo: exercicios_resolvidos\capitulo 09\exercicio-09-11.py
##############################################################################
# Atenção ao encoding no Windows

import sys

if len(sys.argv)!=2:
    print("\nUso: e09-11.py arquivo1\n\n\n")
    sys.exit(1)

nome=sys.argv[1]
contador = {}

arquivo = open(nome, "r",encoding="utf-8")
for linha in arquivo:
    linha = linha.strip().lower()
    palavras = linha.split()
    for p in palavras:
        if p in contador:
            contador[p]+=1
        else:
            contador[p]=1
arquivo.close()

for chave in contador:
    print("%s = %d" % (chave, contador[chave] ))

