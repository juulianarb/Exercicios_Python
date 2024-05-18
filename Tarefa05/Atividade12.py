# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

#  Faça um algoritmo para ler: número da conta do cliente, saldo, débito e crédito. 
# Após, calcular e escrever o saldo atual (saldo atual = saldo - débito + crédito). 
# Também testar se saldo atual for maior ou igual a zero escrever a mensagem 'Saldo Positivo', senão escrever a mensagem 'Saldo Negativo'.

numeroDaconta = int(input("Informe o número da sua conta: "))
saldoDaConta = int(input("Informe o saldo da sua conta: "))
debitoDaConta = int(input("Informe o débito da sua conta: "))
creditoDaConta = int(input("Informe o crédito da sua conta: "))

saldoAtual = saldoDaConta - debitoDaConta + creditoDaConta

if saldoAtual > 0:
    print("Saldo positivo!")
else:
    print("Saldo negativo")
