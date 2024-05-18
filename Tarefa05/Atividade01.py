# Curso básico de python
# Nome do desenvolvedor: Juliana Rodrigues Brito
# Versão 1.0
# Exercício de Lógica de programação com a linguagem python

# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos brancos, nulos e válidos. 
# Calcular e escrever o percentual que cada um representa em relação ao total de eleitores.

eleitores = int(input("Digite o número total de eleitores:"))
votosBrancos = int(input("Digite o número de votos brancos:"))
votosNulos = int(input("Digite o número de votos nulos:"))

votosValidos = eleitores - votosNulos
totalEleitores = eleitores + votosBrancos + votosNulos
porcentagemVotosBrancos = int((totalEleitores * votosBrancos) / 100)
porcentagemVotosNulos = int((totalEleitores * votosNulos) / 100)
porcentagemVotosValidos = int((votosValidos * eleitores) / 100)


print("Total de eleitores: " , totalEleitores)
print("Porcentagem de votos brancos: " , porcentagemVotosBrancos ,"%") 
print("Porcentagem de votos nulos: ", porcentagemVotosNulos,"%")
print("Porcentagem de votos válidos: ", porcentagemVotosValidos, "%")
