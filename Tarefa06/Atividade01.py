# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Ler dois valores numéricos inteiros e apresentar o resultado da diferença do maior pelo menor valor.

primeiroValor = int(input("Digite o primeiro valor inteiro, para ver o resultado da diferença do maior pelo menor: "))
segundoValor = int(input("Digite o segundo valor inteiro, para ver o resultado da diferença do maior pelo menor: "))

resultadoDaDiferenca = abs(primeiroValor - segundoValor)

print("O resultado da diferença entre ", primeiroValor, " e ", segundoValor , ", é de: ", resultadoDaDiferenca)