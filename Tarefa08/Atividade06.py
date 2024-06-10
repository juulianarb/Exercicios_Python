# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Elaborar um programa que apresente como resultado o valor do fatorial dos valores ímpares situados na faixa numérica de 1 a 10.

def fatorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * fatorial(numero - 1)
    
soma_fatoriais = 0

for contadora in range(1, 11):
    if contadora % 2 != 0:
        
        fatorialContadora = fatorial(contadora)
soma_fatoriais += fatorialContadora

print("A soma dos fatoriais dos valores ímpares de 1 a 10 é:", soma_fatoriais)