# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um programa que leia dois números e uma operação (adição, subtração, multiplicação ou divisão) e realize a operação correspondente.

primeiroNumero = float(input("Digite o primeiro número: "))
segundoNumero = float(input("Digite o segundo número: "))
operacao = input("Digite a operação desejada (+ para adição, - para subtração, * para multiplicação, / para divisão): ")

if operacao == '+':
    resultado = primeiroNumero + segundoNumero
    print(f"O resultado da soma é: {resultado}")
elif operacao == '-':
    resultado = primeiroNumero - segundoNumero
    print(f"O resultado da subtração é: {resultado}")
elif operacao == '*':
    resultado = primeiroNumero * segundoNumero
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == '/':
    if segundoNumero != 0:
        resultado = primeiroNumero / segundoNumero
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: divisão por zero.")
else:
    print("Operação inválida. Por favor, digite uma operação válida.")

