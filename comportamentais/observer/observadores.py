# -*- encoding: UTF-8 -*-

def imprime(nota_fiscal):
    print('Imprimindo nota fiscal %s' % (nota_fiscal.cnpj))

def envia_por_email(nota_fiscal):
    print('Enviando nota fiscal %s por email' % (nota_fiscal.cnpj))

def salva_no_banco(nota_fiscal):
    print('Salvando nota fiscal %s no banco' % (nota_fiscal.cnpj))
