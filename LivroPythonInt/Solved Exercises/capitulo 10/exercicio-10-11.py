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
# Arquivo: exercicios_resolvidos\capitulo 10\exercicio-10-11.py
##############################################################################
# Aqui contas.py e clientes.py foram copiados para um só arquivo.
# Esta mudança serve apenas para facilitar a visualização
# da resposta deste exercício.

class Cliente:
     def __init__(self, nome, telefone):
        self.nome = nome
        self.telefone = telefone
# Modifiaque o arquivo contas.py das listagens

class Conta:
    def __init__(self, clientes, número, saldo = 0):
        self.saldo = 0
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)
    def resumo(self):
        print("CC N°%s Saldo: %10.2f" %
               (self.número, self.saldo))
    def saque(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            print("Saldo insuficiente!")
            return False
    def deposito(self, valor):
        self.saldo += valor
        self.operações.append(["DEPÓSITO", valor])
    def extrato(self):
        print("Extrato CC N° %s\n" % self.número)
        for o in self.operações:
            print("%10s   %10.2f" % (o[0],o[1]))
        print("\n      Saldo: %10.2f\n" % self.saldo)


class ContaEspecial(Conta):
    def __init__(self, clientes, número, saldo = 0, limite=0):
        Conta.__init__(self, clientes, número, saldo)
        self.limite = limite
    def saque(self, valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])
            return True
        else:
            return Conta.saque(self, valor)
    def extrato(self):
        Conta.extrato(self)
        print("\n     Limite: %10.2f\n" % self.limite)
        print("\n Disponivel: %10.2f\n" % (self.limite + self.saldo))


josé = Cliente("José", "1243-3321")

conta = ContaEspecial([josé], 3432, 50000, 10000)
conta.extrato()

